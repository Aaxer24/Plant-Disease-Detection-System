"""CLI entrypoint for the DVC "evaluate" stage — see src/models/evaluate.py.

Examples:
    python scripts/evaluate.py
    python scripts/evaluate.py --model-path models/checkpoints/best.keras
    dvc repro evaluate
"""

import argparse
import sys

from src.models.evaluate import run


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model-path", type=str, default=None, help="Path to a .keras model file")
    return parser.parse_args()


if __name__ == "__main__":
    # See scripts/train.py — same Windows console/emoji fix, needed here too
    # since evaluate.py also logs to MLflow.
    if sys.platform == "win32":
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")

    args = parse_args()
    result = run(model_path=args.model_path)
    print(f"\n[OK] Evaluation report: {result['evaluation_path']}")
    print(f"[OK] Figures: {result['figures_dir']}")
