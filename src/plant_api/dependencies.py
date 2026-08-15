"""Dependency injection for services."""

from functools import lru_cache

from src.plant_api.config import get_settings
from src.plant_api.services.chat_service import ChatService
from src.plant_api.services.mlflow_service import MlflowService
from src.plant_api.services.model_service import ModelService


@lru_cache
def get_model_service() -> ModelService:
    """Return singleton ModelService."""
    return ModelService(settings=get_settings())


@lru_cache
def get_chat_service() -> ChatService:
    """Return singleton ChatService."""
    return ChatService(settings=get_settings())


@lru_cache
def get_mlflow_service() -> MlflowService:
    """Return singleton MlflowService."""
    return MlflowService(settings=get_settings())
