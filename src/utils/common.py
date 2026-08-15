"""Shared helpers for the training pipeline: config/params loading and logging."""

import logging
import os

import yaml

PROJECT_ROOT = os.path.join(os.path.dirname(__file__), "..", "..")
DEFAULT_CONFIG_PATH = os.path.join(PROJECT_ROOT, "config", "config.yaml")
DEFAULT_PARAMS_PATH = os.path.join(PROJECT_ROOT, "params.yaml")


def load_config(path: str = DEFAULT_CONFIG_PATH) -> dict:
    """Load config/config.yaml — canonical class list + serving/MLflow defaults."""
    with open(path) as f:
        return yaml.safe_load(f)


def load_params(path: str = DEFAULT_PARAMS_PATH) -> dict:
    """Load root params.yaml — DVC-tracked pipeline hyperparameters."""
    with open(path) as f:
        return yaml.safe_load(f)


def get_class_names(config: dict | None = None) -> list[str]:
    """Canonical class list in label-index order (must match data/processed subfolders)."""
    config = config or load_config()
    return [c["name"] for c in config["classes"]]


def get_logger(name: str) -> logging.Logger:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
    return logging.getLogger(name)
