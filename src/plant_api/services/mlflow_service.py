"""MLflow experiment tracking service."""

import logging
import re
from datetime import datetime, timezone

import mlflow

from src.plant_api.config import Settings

logger = logging.getLogger(__name__)

# MLflow metric/param names only allow alphanumerics, underscores, dashes,
# periods, spaces, colons and slashes — strip everything else (e.g. the
# parentheses in a display name like "Tomato Spider Mites (Two-Spotted)").
_UNSAFE_METRIC_CHARS = re.compile(r"[^a-zA-Z0-9_\-. /:]+")


def _safe_metric_name(name: str) -> str:
    return _UNSAFE_METRIC_CHARS.sub("", name).replace(" ", "_").lower()


class MlflowService:
    """Manages MLflow experiment tracking for model predictions."""

    def __init__(self, settings: Settings) -> None:
        self._settings = settings
        self._setup_mlflow()

    def _setup_mlflow(self) -> None:
        """Configure MLflow tracking URI and experiment."""
        try:
            mlflow.set_tracking_uri(self._settings.MLFLOW_TRACKING_URI)
            mlflow.set_experiment(self._settings.MLFLOW_EXPERIMENT_NAME)
            logger.info(
                "MLflow initialised — uri=%s  experiment=%s",
                self._settings.MLFLOW_TRACKING_URI,
                self._settings.MLFLOW_EXPERIMENT_NAME,
            )
        except Exception:
            logger.warning("MLflow setup failed; tracking disabled", exc_info=True)

    def log_prediction(
        self,
        *,
        predicted_class: str,
        display_name: str,
        confidence: float,
        all_predictions: dict[str, float],
        model_type: str,
        image_size: tuple[int, int] | None = None,
    ) -> None:
        """Log a single inference run to MLflow."""
        try:
            ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
            with mlflow.start_run(run_name=f"prediction_{ts}"):
                mlflow.log_param("predicted_class", predicted_class)
                mlflow.log_param("display_name", display_name)
                mlflow.log_param("model_type", model_type)
                if image_size:
                    mlflow.log_param("image_width", image_size[0])
                    mlflow.log_param("image_height", image_size[1])

                mlflow.log_metric("confidence", confidence)
                for cls, prob in all_predictions.items():
                    mlflow.log_metric(f"prob_{_safe_metric_name(cls)}", prob)

                mlflow.set_tag("timestamp", datetime.now(timezone.utc).isoformat())
                mlflow.set_tag("api_version", "1.0.0")

            logger.debug("MLflow logged: %s (%.1f%%)", predicted_class, confidence)
        except Exception:
            logger.warning("MLflow log failed (non-blocking)", exc_info=True)
