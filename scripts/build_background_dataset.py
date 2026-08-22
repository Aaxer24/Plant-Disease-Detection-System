"""
One-time step to add non-leaf images to the background class.

Run once before running the DVC pipeline:
python -m scripts.build_background_dataset

Then run:
dvc add data/raw/images
dvc push
dvc repro
"""

import argparse
import os
import random
import shutil
import tarfile
import urllib.request

from src.utils.common import PROJECT_ROOT, get_logger

logger = get_logger(__name__)

RAW_DIR = os.path.join(PROJECT_ROOT, "data", "raw", "images")
CLASS_DIR_NAME = "Background___not_a_leaf"
IMAGENETTE_URL = "https://s3.amazonaws.com/fast-ai-imageclas/imagenette2-160.tgz"
CACHE_DIR = os.path.join(PROJECT_ROOT, ".cache", "imagenette")
ARCHIVE_PATH = os.path.join(CACHE_DIR, "imagenette2-160.tgz")
EXTRACT_DIR = os.path.join(CACHE_DIR, "imagenette2-160")


def build(images_per_class: int = 120, seed: int = 123) -> None:
    """Download `imagenette`, then write a balanced sample into the background class folder."""
    os.makedirs(CACHE_DIR, exist_ok=True)
    if not os.path.exists(ARCHIVE_PATH):
        logger.info("Downloading %s ...", IMAGENETTE_URL)
        urllib.request.urlretrieve(IMAGENETTE_URL, ARCHIVE_PATH)
    else:
        logger.info("Archive already downloaded: %s", ARCHIVE_PATH)

    if not os.path.isdir(EXTRACT_DIR):
        logger.info("Extracting archive...")
        with tarfile.open(ARCHIVE_PATH) as tar:
            tar.extractall(CACHE_DIR)
    else:
        logger.info("Already extracted: %s", EXTRACT_DIR)

    train_dir = os.path.join(EXTRACT_DIR, "train")
    source_classes = sorted(
        d for d in os.listdir(train_dir) if os.path.isdir(os.path.join(train_dir, d))
    )

    out_dir = os.path.join(RAW_DIR, CLASS_DIR_NAME)
    os.makedirs(out_dir, exist_ok=True)

    rng = random.Random(seed)
    written = 0
    for source_class in source_classes:
        class_dir = os.path.join(train_dir, source_class)
        files = sorted(f for f in os.listdir(class_dir) if f.lower().endswith((".jpeg", ".jpg")))
        rng.shuffle(files)
        chosen = files[:images_per_class]

        for i, filename in enumerate(chosen):
            dst = os.path.join(out_dir, f"imagenette_{source_class}_{i:04d}.jpg")
            shutil.copy2(os.path.join(class_dir, filename), dst)
            written += 1

        logger.info("%s: %d images copied", source_class, len(chosen))

    logger.info("Done — %d background images written to %s", written, out_dir)
    logger.info(
        "Next steps: config/config.yaml's '%s' class is already in place; "
        "now run `dvc add data/raw/images`, `dvc push`, then retrain.",
        CLASS_DIR_NAME,
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--images-per-class",
        type=int,
        default=120,
        help="How many images to sample per imagenette source class (default: 120, ~1200 total)",
    )
    args = parser.parse_args()
    build(images_per_class=args.images_per_class)
