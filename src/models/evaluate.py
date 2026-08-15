"""DVC "evaluate" stage: scores models/model.keras on data/processed/test and
writes reports/evaluation.txt + reports/figures/{confusion_matrix,sample_predictions,
training_curve}.png.

If train.py logged a run (models/.mlflow_run_id), this resumes that SAME MLflow
run to attach the report/figures there too — so one run holds the full picture:
hyperparameters, training curves, the registered model, and eval results.

Run via:
    python -m src.models.evaluate
    dvc repro evaluate
"""

import os

import matplotlib

matplotlib.use("Agg")
import json

import matplotlib.pyplot as plt
import mlflow
import numpy as np
import tensorflow as tf
from sklearn.metrics import ConfusionMatrixDisplay, classification_report, confusion_matrix

from src.data.preprocess import load_split
from src.utils.common import PROJECT_ROOT, get_logger, load_config, load_params

logger = get_logger(__name__)

PROCESSED_DIR = os.path.join(PROJECT_ROOT, "data", "processed")
REPORTS_DIR = os.path.join(PROJECT_ROOT, "reports")
FIGURES_DIR = os.path.join(REPORTS_DIR, "figures")


def _plot_training_curve(history: dict, output_path: str) -> None:
    epochs_range = range(len(history["loss"]))

    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.plot(epochs_range, history["accuracy"], label="Training Accuracy")
    plt.plot(epochs_range, history["val_accuracy"], label="Validation Accuracy")
    plt.legend(loc="lower right")
    plt.title("Training and Validation Accuracy")
    plt.xlabel("Epoch")

    plt.subplot(1, 2, 2)
    plt.plot(epochs_range, history["loss"], label="Training Loss")
    plt.plot(epochs_range, history["val_loss"], label="Validation Loss")
    plt.legend(loc="upper right")
    plt.title("Training and Validation Loss")
    plt.xlabel("Epoch")

    plt.tight_layout()
    plt.savefig(output_path, dpi=120)
    plt.close()


def _plot_confusion_matrix(y_true, y_pred, class_names: list[str], output_path: str) -> None:
    cm = confusion_matrix(y_true, y_pred, labels=range(len(class_names)))
    fig, ax = plt.subplots(figsize=(12, 12))
    display = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=class_names)
    display.plot(ax=ax, xticks_rotation=90, colorbar=False, cmap="Blues")
    plt.tight_layout()
    plt.savefig(output_path, dpi=120)
    plt.close()


def _plot_sample_predictions(model, test_ds, class_names: list[str], output_path: str) -> None:
    plt.figure(figsize=(15, 15))
    for images, labels in test_ds.take(1):
        predictions = model.predict(images, verbose=0)
        num_samples = min(9, images.shape[0])
        for i in range(num_samples):
            plt.subplot(3, 3, i + 1)
            plt.imshow(images[i].numpy().astype("uint8"))
            predicted_idx = int(np.argmax(predictions[i]))
            confidence = round(100 * float(np.max(predictions[i])), 2)
            actual = class_names[int(labels[i])]
            predicted = class_names[predicted_idx]
            plt.title(
                f"Actual: {actual}\nPredicted: {predicted}\nConfidence: {confidence}%", fontsize=8
            )
            plt.axis("off")
    plt.tight_layout()
    plt.savefig(output_path, dpi=120)
    plt.close()


def _log_to_mlflow(
    config: dict, models_dir: str, report_dict: dict, artifact_paths: list[str]
) -> None:
    """Resume train.py's MLflow run (if any) to attach eval metrics + figures."""
    run_id_path = os.path.join(models_dir, ".mlflow_run_id")
    if not os.path.exists(run_id_path):
        logger.info("No models/.mlflow_run_id found; skipping MLflow logging for evaluate stage")
        return

    with open(run_id_path) as f:
        run_id = f.read().strip()

    tracking_uri = os.environ.get("MLFLOW_TRACKING_URI") or config.get(
        "mlflow_tracking_uri", "mlruns"
    )
    try:
        mlflow.set_tracking_uri(tracking_uri)
        with mlflow.start_run(run_id=run_id):
            mlflow.log_metric("eval_accuracy", report_dict["accuracy"])
            for avg in ("macro avg", "weighted avg"):
                safe_avg = avg.replace(" ", "_")
                for metric_name in ("precision", "recall", "f1-score"):
                    mlflow.log_metric(
                        f"eval_{safe_avg}_{metric_name.replace('-', '_')}",
                        report_dict[avg][metric_name],
                    )
            for path in artifact_paths:
                if os.path.exists(path):
                    mlflow.log_artifact(path)
        logger.info("Logged evaluation results to MLflow run %s", run_id)
    except Exception:
        logger.warning("MLflow logging failed for evaluate stage (non-blocking)", exc_info=True)


def run(model_path: str | None = None) -> dict:
    config = load_config()
    params = load_params()["train"]

    models_dir = os.path.join(PROJECT_ROOT, config.get("model_dir", "models"))
    model_path = model_path or os.path.join(
        models_dir, f"{config.get('model_name', 'plant_disease_model')}.keras"
    )

    os.makedirs(FIGURES_DIR, exist_ok=True)

    logger.info("Loading model from %s", model_path)
    model = tf.keras.models.load_model(model_path)

    logger.info("Loading test split from %s", os.path.join(PROCESSED_DIR, "test"))
    test_ds, class_names = load_split(
        os.path.join(PROCESSED_DIR, "test"),
        image_size=params["image_size"],
        batch_size=params["batch_size"],
        seed=params["seed"],
        shuffle=False,
    )

    y_true, y_pred = [], []
    for images, labels in test_ds:
        predictions = model.predict(images, verbose=0)
        y_true.extend(labels.numpy().tolist())
        y_pred.extend(np.argmax(predictions, axis=1).tolist())

    report_text = classification_report(y_true, y_pred, target_names=class_names, zero_division=0)
    report_dict = classification_report(
        y_true, y_pred, target_names=class_names, zero_division=0, output_dict=True
    )
    logger.info("\n%s", report_text)

    evaluation_path = os.path.join(REPORTS_DIR, "evaluation.txt")
    with open(evaluation_path, "w") as f:
        f.write(report_text)

    confusion_matrix_path = os.path.join(FIGURES_DIR, "confusion_matrix.png")
    sample_predictions_path = os.path.join(FIGURES_DIR, "sample_predictions.png")
    training_curve_path = os.path.join(FIGURES_DIR, "training_curve.png")

    _plot_confusion_matrix(y_true, y_pred, class_names, confusion_matrix_path)
    _plot_sample_predictions(model, test_ds, class_names, sample_predictions_path)

    history_path = os.path.join(REPORTS_DIR, "training_history.json")
    if os.path.exists(history_path):
        with open(history_path) as f:
            history = json.load(f)
        _plot_training_curve(history["history"], training_curve_path)
    else:
        logger.warning("No reports/training_history.json found; skipping training curve plot")

    _log_to_mlflow(
        config,
        models_dir,
        report_dict,
        [evaluation_path, confusion_matrix_path, sample_predictions_path, training_curve_path],
    )

    logger.info("Reports written to %s", REPORTS_DIR)
    return {"evaluation_path": evaluation_path, "figures_dir": FIGURES_DIR}


if __name__ == "__main__":
    run()
