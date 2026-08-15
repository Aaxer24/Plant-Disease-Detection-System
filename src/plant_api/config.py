import os
from functools import lru_cache

import yaml
from pydantic_settings import BaseSettings, SettingsConfigDict

_PROJECT_ROOT = os.path.join(os.path.dirname(__file__), "..", "..")
_CONFIG_FILE = os.path.join(_PROJECT_ROOT, "config", "config.yaml")


def _load_config(path: str) -> dict:
    with open(path) as f:
        return yaml.safe_load(f)


_CONFIG = _load_config(_CONFIG_FILE)
_CLASS_NAMES = [c["name"] for c in _CONFIG["classes"]]
_DISPLAY_NAMES = {c["name"]: c["display_name"] for c in _CONFIG["classes"]}


class Settings(BaseSettings):
    GROQ_API_KEY: str = ""
    GROQ_MODEL: str = "openai/gpt-oss-120b"
    MODEL_DIR: str = os.path.join(_PROJECT_ROOT, _CONFIG.get("model_dir", "models"))
    MODEL_NAME: str = _CONFIG.get("model_name", "plant_disease_model")
    IMAGE_SIZE: int = 256
    CLASS_NAMES: list[str] = _CLASS_NAMES
    DISPLAY_NAMES: dict[str, str] = _DISPLAY_NAMES
    MLFLOW_TRACKING_URI: str = _CONFIG.get("mlflow_tracking_uri", "mlruns")
    MLFLOW_EXPERIMENT_NAME: str = _CONFIG.get("mlflow_experiment_name", "plant-disease-detection")
    LOG_LEVEL: str = "INFO"
    CORS_ORIGINS: list[str] = ["*"]

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


@lru_cache
def get_settings() -> Settings:
    return Settings()
