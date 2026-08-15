"""CNN architecture for multi-crop plant disease classification."""

import tensorflow as tf
from tensorflow.keras import layers, models

from src.data.preprocess import build_preprocessing_layers


def build_model(num_classes: int, image_size: int, channels: int = 3) -> tf.keras.Model:
    """Build the classifier: a 6-block Conv2D/MaxPooling stack over resize+augment layers."""
    resize_and_rescale, data_augmentation = build_preprocessing_layers(image_size)
    input_shape = (image_size, image_size, channels)

    model = models.Sequential(
        [
            layers.Input(shape=input_shape),
            resize_and_rescale,
            data_augmentation,
            layers.Conv2D(32, kernel_size=(3, 3), activation="relu"),
            layers.MaxPooling2D((2, 2)),
            layers.Conv2D(64, kernel_size=(3, 3), activation="relu"),
            layers.MaxPooling2D((2, 2)),
            layers.Conv2D(64, kernel_size=(3, 3), activation="relu"),
            layers.MaxPooling2D((2, 2)),
            layers.Conv2D(64, kernel_size=(3, 3), activation="relu"),
            layers.MaxPooling2D((2, 2)),
            layers.Conv2D(64, kernel_size=(3, 3), activation="relu"),
            layers.MaxPooling2D((2, 2)),
            layers.Conv2D(64, kernel_size=(3, 3), activation="relu"),
            layers.MaxPooling2D((2, 2)),
            layers.Flatten(),
            layers.Dense(64, activation="relu"),
            layers.Dense(num_classes, activation="softmax"),
        ]
    )
    return model
