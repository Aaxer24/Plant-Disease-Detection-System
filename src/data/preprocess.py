"""Loads the materialized train/val/test splits (data/processed/*) for training."""

import os

import tensorflow as tf
from tensorflow.keras import layers

AUTOTUNE = tf.data.AUTOTUNE


def load_split(
    split_dir: str, image_size: int, batch_size: int, seed: int, shuffle: bool = True
) -> tuple[tf.data.Dataset, list[str]]:
    """Load one split directory (class-per-folder) as a batched, prefetched dataset.

    Deliberately NOT cached (neither in memory nor to disk): at tens of
    thousands of images, TF's decoded float32 tensors need tens of GB either
    way — more than this machine's RAM or free disk. Images are decoded fresh
    each epoch instead; prefetch(AUTOTUNE) still overlaps that decode with the
    previous batch's training step so it isn't a hard serial bottleneck.
    """
    dataset = tf.keras.utils.image_dataset_from_directory(
        split_dir,
        seed=seed,
        shuffle=shuffle,
        image_size=(image_size, image_size),
        batch_size=batch_size,
    )
    class_names = dataset.class_names
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
    """Resize/rescale + augmentation layers, applied inside the model graph.

    Rescales to [-1, 1] (not [0, 1]) — this matches what MobileNetV2's ImageNet
    weights expect (equivalent to tf.keras.applications.mobilenet_v2.preprocess_input
    for standard 0-255 inputs), since build_model() uses MobileNetV2 as its backbone.
    """
    resize_and_rescale = tf.keras.Sequential(
        [
            layers.Resizing(image_size, image_size),
            layers.Rescaling(1.0 / 127.5, offset=-1),
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
