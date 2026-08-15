"""DVC "train" stage: trains the classifier on data/processed/{train,val}.

Saves models/{model_name}.keras + models/checkpoints/best.keras locally (loaded
by the serving API), and — when MLflow is reachable — logs params/metrics and
registers the model as a new version under MLflow's Model Registry. DVC does
not cache or version the model file itself; that's MLflow's job here.

Run via:
    python -m src.models.train
    dvc repro train
"""

import json
import os
from datetime import datetime, timezone

import mlflow
import mlflow.keras
import tensorflow as tf

from src.data.preprocess import load_datasets
from src.models.model import build_model
from src.utils.common import PROJECT_ROOT, get_class_names, get_logger, load_config, load_params

logger = get_logger(__name__)

PROCESSED_DIR = os.path.join(PROJECT_ROOT, "data", "processed")
CHECKPOINTS_DIR = os.path.join(PROJECT_ROOT, "models", "checkpoints")
LOGS_DIR = os.path.join(PROJECT_ROOT, "logs", "training")
REPORTS_DIR = os.path.join(PROJECT_ROOT, "reports")


class MlflowEpochLogger(tf.keras.callbacks.Callback):
    """Streams per-epoch metrics to the active MLflow run."""

    def on_epoch_end(self, epoch, logs=None):
        for key, value in (logs or {}).items():
            mlflow.log_metric(key, float(value), step=epoch)


def run(param_overrides: dict | None = None) -> dict:
    config = load_config()
    params = load_params()["train"]
    params.update({k: v for k, v in (param_overrides or {}).items() if v is not None})
    class_names = get_class_names(config)

    logger.info("Loading processed dataset from %s", PROCESSED_DIR)
    train_ds, val_ds, test_ds, dataset_class_names = load_datasets(
        PROCESSED_DIR,
        image_size=params["image_size"],
        batch_size=params["batch_size"],
        seed=params["seed"],
    )

    if dataset_class_names != class_names:
        raise ValueError(
            "data/processed/train class order does not match config/config.yaml.\n"
            f"  dataset:   {dataset_class_names}\n"
            f"  canonical: {class_names}\n"
            "Run `python -m src.data.make_dataset` again, or update config/config.yaml."
        )

    num_classes = len(class_names)
    logger.info("Found %d classes: %s", num_classes, class_names)

    model = build_model(num_classes, params["image_size"], params["channels"])
    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=params["learning_rate"]),
        loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),
        metrics=["accuracy"],
    )

    os.makedirs(CHECKPOINTS_DIR, exist_ok=True)
    os.makedirs(REPORTS_DIR, exist_ok=True)
    run_timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    tensorboard_dir = os.path.join(LOGS_DIR, run_timestamp)
    os.makedirs(tensorboard_dir, exist_ok=True)

    checkpoint_path = os.path.join(CHECKPOINTS_DIR, "best.keras")
    callbacks = [
        tf.keras.callbacks.EarlyStopping(
            monitor="val_accuracy",
            patience=params["early_stopping_patience"],
            restore_best_weights=True,
        ),
        tf.keras.callbacks.ModelCheckpoint(
            checkpoint_path, monitor="val_accuracy", save_best_only=True
        ),
        tf.keras.callbacks.TensorBoard(log_dir=tensorboard_dir),
    ]

    mlflow_active = True
    tracking_uri = os.environ.get("MLFLOW_TRACKING_URI") or config.get(
        "mlflow_tracking_uri", "mlruns"
    )
    try:
        mlflow.set_tracking_uri(tracking_uri)
        mlflow.set_experiment(
            config.get("mlflow_training_experiment_name", "plant-disease-training")
        )
    except Exception:
        logger.warning(
            "MLflow setup failed (tracking_uri=%s); continuing without tracking",
            tracking_uri,
            exc_info=True,
        )
        mlflow_active = False

    if mlflow_active:
        run_ctx = mlflow.start_run(run_name=f"train_{run_timestamp}")
    else:
        from contextlib import nullcontext

        run_ctx = nullcontext()

    mlflow_run_id = None
    with run_ctx:
        if mlflow_active:
            mlflow_run_id = mlflow.active_run().info.run_id
            mlflow.log_params(params)
            mlflow.log_param("num_classes", num_classes)
            callbacks.append(MlflowEpochLogger())

        history = model.fit(
            train_ds,
            validation_data=val_ds,
            epochs=params["epochs"],
            callbacks=callbacks,
            verbose=1,
        )

        logger.info("Evaluating on held-out test set")
        test_loss, test_accuracy = model.evaluate(test_ds, verbose=1)
        logger.info("Test accuracy: %.4f  Test loss: %.4f", test_accuracy, test_loss)

        if mlflow_active:
            mlflow.log_metric("test_accuracy", test_accuracy)
            mlflow.log_metric("test_loss", test_loss)

        model_name = config.get("model_name", "plant_disease_model")
        models_dir = os.path.join(PROJECT_ROOT, config.get("model_dir", "models"))
        model_path = os.path.join(models_dir, f"{model_name}.keras")
        model.save(model_path)

        if mlflow_active:
            try:
                mlflow.keras.log_model(
                    model, artifact_path="model", registered_model_name=model_name
                )
            except Exception:
                logger.warning("MLflow model registration failed (non-blocking)", exc_info=True)

        epochs_ran = len(history.history["loss"])

        history_path = os.path.join(REPORTS_DIR, "training_history.json")
        with open(history_path, "w") as f:
            json.dump(
                {
                    "test_accuracy": float(test_accuracy),
                    "test_loss": float(test_loss),
                    "epochs_ran": epochs_ran,
                    "class_names": class_names,
                    "history": {k: [float(v) for v in vals] for k, vals in history.history.items()},
                },
                f,
                indent=2,
            )

        # Flat scalar metrics for `dvc metrics diff` (dvc.yaml declares this as a metrics file).
        metrics_path = os.path.join(REPORTS_DIR, "metrics.json")
        with open(metrics_path, "w") as f:
            json.dump(
                {
                    "test_accuracy": float(test_accuracy),
                    "test_loss": float(test_loss),
                    "epochs_ran": epochs_ran,
                },
                f,
                indent=2,
            )

        if mlflow_active:
            mlflow.log_artifact(history_path)
            mlflow.log_artifact(metrics_path)

    # Hand the run ID to evaluate.py (run separately by dvc.yaml) so its report
    # and figures land in the SAME MLflow run instead of a disconnected one.
    run_id_path = os.path.join(models_dir, ".mlflow_run_id")
    if mlflow_run_id:
        with open(run_id_path, "w") as f:
            f.write(mlflow_run_id)
    elif os.path.exists(run_id_path):
        os.remove(run_id_path)

    logger.info("Model saved to %s  (best checkpoint: %s)", model_path, checkpoint_path)
    return {
        "test_accuracy": float(test_accuracy),
        "test_loss": float(test_loss),
        "model_path": model_path,
        "mlflow_run_id": mlflow_run_id,
    }


if __name__ == "__main__":
    run()
