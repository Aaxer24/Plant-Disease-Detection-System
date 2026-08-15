"""Loads the materialized train/val/test splits (data/processed/*) for training."""

import os

import tensorflow as tf
from tensorflow.keras import layers

AUTOTUNE = tf.data.AUTOTUNE


def load_split(
    split_dir: str, image_size: int, batch_size: int, seed: int, shuffle: bool = True
) -> tuple[tf.data.Dataset, list[str]]:
    """Load one split directory (class-per-folder) as a batched, cached, prefetched dataset."""
    dataset = tf.keras.utils.image_dataset_from_directory(
        split_dir,
        seed=seed,
        shuffle=shuffle,
        image_size=(image_size, image_size),
        batch_size=batch_size,
    )
    class_names = dataset.class_names
    dataset = dataset.cache()
    if shuffle:
        dataset = dataset.shuffle(1000, seed=seed)
    dataset = dataset.prefetch(buffer_size=AUTOTUNE)
    return dataset, class_names


def load_datasets(
    processed_dir: str, image_size: int, batch_size: int, seed: int
) -> tuple[tf.data.Dataset, tf.data.Dataset, tf.data.Dataset, list[str]]:
    """Load train/val/test splits from data/processed/{train,val,test}."""
    train_ds, class_names = load_split(
        os.path.join(processed_dir, "train"), image_size, batch_size, seed
    )
    val_ds, _ = load_split(
        os.path.join(processed_dir, "val"), image_size, batch_size, seed, shuffle=False
    )
    test_ds, _ = load_split(
        os.path.join(processed_dir, "test"), image_size, batch_size, seed, shuffle=False
    )
    return train_ds, val_ds, test_ds, class_names


def build_preprocessing_layers(image_size: int) -> tuple[tf.keras.Sequential, tf.keras.Sequential]:
    """Resize/rescale + augmentation layers, applied inside the model graph."""
    resize_and_rescale = tf.keras.Sequential(
        [
            layers.Resizing(image_size, image_size),
            layers.Rescaling(1.0 / 255),
        ],
        name="resize_and_rescale",
    )
    data_augmentation = tf.keras.Sequential(
        [
            layers.RandomFlip("horizontal_and_vertical"),
            layers.RandomRotation(0.2),
        ],
        name="data_augmentation",
    )
    return resize_and_rescale, data_augmentation
