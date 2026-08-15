"""CLI entrypoint for the DVC "train" stage — see src/models/train.py.

Normal usage relies on params.yaml (edit it, or `dvc exp run --set-param`) so the
pipeline stays reproducible. The flags below are a convenience for quick local
sanity checks and override params.yaml for this run only — they are not persisted.

Examples:
    python scripts/train.py
    python scripts/train.py --epochs 2 --batch-size 16     # quick smoke test
    dvc repro train
"""

import argparse
import sys

from src.models.train import run


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--epochs", type=int, default=None)
    parser.add_argument("--batch-size", type=int, default=None)
    parser.add_argument("--image-size", type=int, default=None)
    parser.add_argument("--learning-rate", type=float, default=None)
    return parser.parse_args()


if __name__ == "__main__":
    # MLflow prints emoji (e.g. "View run") on successful completion — Windows'
    # default console codepage can't encode them, which would otherwise crash
    # the script right at the finish line despite training having succeeded.
    if sys.platform == "win32":
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")

    args = parse_args()
    overrides = {
        "epochs": args.epochs,
        "batch_size": args.batch_size,
        "image_size": args.image_size,
        "learning_rate": args.learning_rate,
    }
    result = run(overrides)
    print(f"\n[OK] Test accuracy: {result['test_accuracy'] * 100:.2f}%")
    print(f"[OK] Model saved to: {result['model_path']}")
