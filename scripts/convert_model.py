"""Convert Keras model to optimised TFLite for production inference."""

import os

import tensorflow as tf

from src.utils.common import PROJECT_ROOT, load_config


def convert_keras_to_tflite() -> None:
    """Convert models/{model_name}.keras -> models/{model_name}.tflite (default optimisations)."""
    config = load_config()
    models_dir = os.path.join(PROJECT_ROOT, config.get("model_dir", "models"))
    model_name = config.get("model_name", "plant_disease_model")
    keras_path = os.path.join(models_dir, f"{model_name}.keras")
    tflite_path = os.path.join(models_dir, f"{model_name}.tflite")

    print(f"Loading Keras model from: {keras_path}")
    original = tf.keras.models.load_model(keras_path)

    # Fix batch size = 1 for API / mobile inference
    print("Adapting for batch_size=1...")
    input_shape = original.input_shape[1:]
    inputs = tf.keras.Input(shape=input_shape, batch_size=1)
    outputs = original(inputs)
    model = tf.keras.Model(inputs=inputs, outputs=outputs)

    print("Converting to TFLite...")
    converter = tf.lite.TFLiteConverter.from_keras_model(model)
    converter.optimizations = [tf.lite.Optimize.DEFAULT]
    tflite_model = converter.convert()

    with open(tflite_path, "wb") as f:
        f.write(tflite_model)

    mb = os.path.getsize(tflite_path) / (1024 * 1024)
    print(f"\n[OK] Saved: {tflite_path}  ({mb:.2f} MB)")


if __name__ == "__main__":
    convert_keras_to_tflite()
