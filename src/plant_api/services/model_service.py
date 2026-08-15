"""Keras inference service."""

import io
import logging
import os

import numpy as np
import PIL.Image

from src.plant_api.config import Settings

logger = logging.getLogger(__name__)


class ModelService:
    """Loads the ML model and runs disease predictions."""

    def __init__(self, settings: Settings) -> None:
        self._settings = settings
        self._keras_model = None
        self._load_model()

    def _load_model(self) -> None:
        keras_path = os.path.join(self._settings.MODEL_DIR, f"{self._settings.MODEL_NAME}.keras")

        try:
            import tensorflow as tf

            self._keras_model = tf.keras.models.load_model(keras_path)
            logger.info("Keras model loaded from %s", keras_path)
        except Exception:
            logger.error(
                "Failed to load model from %s",
                self._settings.MODEL_DIR,
                exc_info=True,
            )

    @property
    def model_loaded(self) -> bool:
        return self._keras_model is not None

    def preprocess_image(self, image_bytes: bytes) -> np.ndarray:
        """Decode, resize and batch an image."""
        img = PIL.Image.open(io.BytesIO(image_bytes)).convert("RGB")
        img = img.resize((self._settings.IMAGE_SIZE, self._settings.IMAGE_SIZE))
        arr = np.array(img)
        return np.expand_dims(arr, axis=0)

    def predict(self, image_bytes: bytes) -> dict:
        """Run inference and return structured prediction dict."""
        if not self.model_loaded:
            raise RuntimeError("No model loaded")

        image_array = self.preprocess_image(image_bytes)
        predictions = self._keras_model.predict(image_array)[0]

        idx = int(np.argmax(predictions))
        confidence = round(float(predictions[idx]) * 100, 2)
        predicted_class = self._settings.CLASS_NAMES[idx]
        display_name = self._settings.DISPLAY_NAMES.get(predicted_class, predicted_class)

        all_predictions = {
            self._settings.DISPLAY_NAMES.get(
                self._settings.CLASS_NAMES[i], self._settings.CLASS_NAMES[i]
            ): round(float(predictions[i]) * 100, 2)
            for i in range(len(self._settings.CLASS_NAMES))
        }

        return {
            "class": predicted_class,
            "display_name": display_name,
            "confidence": confidence,
            "all_predictions": all_predictions,
            "model_type": "keras",
        }
