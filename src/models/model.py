"""MobileNetV2 transfer-learning architecture for multi-crop plant disease classification."""

import tensorflow as tf
from tensorflow.keras import layers, models

from src.data.preprocess import build_preprocessing_layers


def build_model(num_classes: int, image_size: int, channels: int = 3) -> tf.keras.Model:
    """Build the classifier: a frozen, ImageNet-pretrained MobileNetV2 backbone with a
    small trainable classification head on top, over resize+rescale+augment layers.

    The backbone is frozen (not fine-tuned) — it already knows general visual features
    (edges, textures, shapes) from ImageNet, so only the small head needs training. This
    converges in far fewer epochs than training a CNN from scratch, which matters here
    since training runs on CPU.
    """
    resize_and_rescale, data_augmentation = build_preprocessing_layers(image_size)
    input_shape = (image_size, image_size, channels)

    base_model = tf.keras.applications.MobileNetV2(
        input_shape=input_shape, include_top=False, weights="imagenet"
    )
    base_model.trainable = False

    model = models.Sequential(
        [
            layers.Input(shape=input_shape),
            resize_and_rescale,
            data_augmentation,
            base_model,
            layers.GlobalAveragePooling2D(),
            layers.Dropout(0.2),
            layers.Dense(128, activation="relu"),
            layers.Dense(num_classes, activation="softmax"),
        ]
    )
    return model
