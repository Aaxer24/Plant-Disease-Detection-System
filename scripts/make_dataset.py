"""CLI entrypoint for the DVC "prepare" stage — see src/data/make_dataset.py."""

from src.data.make_dataset import make_dataset

if __name__ == "__main__":
    counts = make_dataset()
    print(f"\n[OK] train: {counts['train']}  val: {counts['val']}  test: {counts['test']}")
