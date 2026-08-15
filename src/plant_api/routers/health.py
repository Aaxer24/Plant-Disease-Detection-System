"""Health and root endpoints."""

from fastapi import APIRouter, Depends

from src.plant_api import __version__
from src.plant_api.dependencies import get_model_service
from src.plant_api.schemas.api_schemas import HealthResponse
from src.plant_api.services.model_service import ModelService

router = APIRouter(tags=["health"])


@router.get("/")
async def root():
    return {
        "message": "🌿 Plant Disease Detection API",
        "version": __version__,
        "endpoints": {
            "/predict": "POST - Upload image for disease detection",
            "/chat": "POST - Chat with AI about plant diseases",
            "/health": "GET - Health check",
        },
    }


@router.get("/health", response_model=HealthResponse)
async def health_check(
    model_service: ModelService = Depends(get_model_service),
):
    return HealthResponse(
        status="healthy",
        model_loaded=model_service.model_loaded,
        version=__version__,
    )
