"""DVC "prepare" stage: split data/raw/images/<class>/* into
data/processed/{train,val,test}/<class>/* using hardlinks (no extra disk usage —
raw and processed reference the same file data on disk).

Run via:
    python -m src.data.make_dataset
    dvc repro prepare
"""

import os
import random
import shutil

from src.utils.common import PROJECT_ROOT, get_logger, load_config, load_params

logger = get_logger(__name__)

RAW_DIR = os.path.join(PROJECT_ROOT, "data", "raw", "images")
PROCESSED_DIR = os.path.join(PROJECT_ROOT, "data", "processed")
SPLITS = ("train", "val", "test")


def _link_or_copy(src_path: str, dst_path: str) -> None:
    """Hardlink when possible (same volume, zero extra disk); fall back to copy."""
    try:
        os.link(src_path, dst_path)
    except OSError:
        shutil.copy2(src_path, dst_path)


def make_dataset(raw_dir: str = RAW_DIR, processed_dir: str = PROCESSED_DIR) -> dict:
    """Split each class folder under raw_dir into train/val/test under processed_dir."""
    config = load_config()
    canonical_classes = sorted(c["name"] for c in config["classes"])

    raw_classes = sorted(d for d in os.listdir(raw_dir) if os.path.isdir(os.path.join(raw_dir, d)))
    if raw_classes != canonical_classes:
        raise ValueError(
            "data/raw/images class folders do not match config/config.yaml.\n"
            f"  raw:       {raw_classes}\n"
            f"  canonical: {canonical_classes}"
        )

    params = load_params()["prepare"]
    train_split, val_split, test_split = (
        params["train_split"],
        params["val_split"],
        params["test_split"],
    )
    assert abs((train_split + val_split + test_split) - 1.0) < 1e-6

    rng = random.Random(params["seed"])

    # Clean slate so re-running is idempotent (e.g. after changing split ratios).
    for split in SPLITS:
        split_dir = os.path.join(processed_dir, split)
        if os.path.exists(split_dir):
            shutil.rmtree(split_dir)
        os.makedirs(split_dir, exist_ok=True)

    counts = {split: 0 for split in SPLITS}
    for class_name in canonical_classes:
        files = sorted(os.listdir(os.path.join(raw_dir, class_name)))
        rng.shuffle(files)

        n = len(files)
        n_train = int(train_split * n)
        n_val = int(val_split * n)
        split_files = {
            "train": files[:n_train],
            "val": files[n_train : n_train + n_val],
            "test": files[n_train + n_val :],
        }

        for split, split_file_list in split_files.items():
            out_dir = os.path.join(processed_dir, split, class_name)
            os.makedirs(out_dir, exist_ok=True)
            for filename in split_file_list:
                _link_or_copy(
                    os.path.join(raw_dir, class_name, filename),
                    os.path.join(out_dir, filename),
                )
            counts[split] += len(split_file_list)

        logger.info(
            "%s: %d train / %d val / %d test",
            class_name,
            len(split_files["train"]),
            len(split_files["val"]),
            len(split_files["test"]),
        )

    logger.info(
        "Total — train: %d  val: %d  test: %d", counts["train"], counts["val"], counts["test"]
    )
    return counts


if __name__ == "__main__":
    make_dataset()
