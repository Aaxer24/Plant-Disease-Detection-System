"""Shared pytest fixtures."""

from unittest.mock import AsyncMock, MagicMock

import pytest
from fastapi.testclient import TestClient

from src.plant_api.dependencies import get_chat_service, get_mlflow_service, get_model_service
from src.plant_api.main import app
from src.plant_api.schemas.api_schemas import ChatResponse


@pytest.fixture()
def mock_model_service():
    """Mock ModelService — returns a fixed healthy prediction."""
    svc = MagicMock()
    svc.model_loaded = True
    svc.predict.return_value = {
        "class": "Potato___healthy",
        "display_name": "Healthy",
        "confidence": 98.5,
        "all_predictions": {"Early Blight": 0.5, "Late Blight": 1.0, "Healthy": 98.5},
        "model_type": "tflite",
    }
    return svc


@pytest.fixture()
def mock_chat_service():
    """Mock ChatService — returns a fixed chat response."""
    svc = MagicMock()
    svc.chat = AsyncMock(
        return_value=ChatResponse(
            response="Your potato plant looks healthy! Keep it up 🌱",
            disease_context=None,
        )
    )

    async def _fake_stream(*args, **kwargs):
        for chunk in ["Your potato plant ", "looks healthy! ", "Keep it up 🌱"]:
            yield chunk

    svc.stream_chat = _fake_stream
    return svc


@pytest.fixture()
def mock_mlflow_service():
    """Mock MlflowService — silently accepts log calls."""
    svc = MagicMock()
    svc.log_prediction = MagicMock()
    return svc


@pytest.fixture()
def client(mock_model_service, mock_chat_service, mock_mlflow_service):
    """FastAPI TestClient with all services mocked (no GPU/API keys needed)."""
    app.dependency_overrides[get_model_service] = lambda: mock_model_service
    app.dependency_overrides[get_chat_service] = lambda: mock_chat_service
    app.dependency_overrides[get_mlflow_service] = lambda: mock_mlflow_service

    with TestClient(app) as c:
        yield c

    app.dependency_overrides.clear()
