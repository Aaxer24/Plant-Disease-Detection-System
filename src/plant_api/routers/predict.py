"""Prediction endpoint."""

import logging

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile

from src.plant_api.dependencies import get_mlflow_service, get_model_service
from src.plant_api.knowledge.knowledge_base import PLANT_DISEASE_KNOWLEDGE
from src.plant_api.schemas.api_schemas import PredictionResponse
from src.plant_api.services.mlflow_service import MlflowService
from src.plant_api.services.model_service import ModelService

logger = logging.getLogger(__name__)

router = APIRouter(tags=["prediction"])


@router.post("/predict", response_model=PredictionResponse)
async def predict_disease(
    file: UploadFile = File(...),
    model_service: ModelService = Depends(get_model_service),
    mlflow_service: MlflowService = Depends(get_mlflow_service),
):
    """Upload a plant leaf image (potato, tomato or pepper) and get disease prediction."""
    if not file.content_type or not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Please upload an image file (JPEG, PNG)")

    try:
        image_bytes = await file.read()
        prediction = model_service.predict(image_bytes)

        # Log to MLflow (fire-and-forget, failures are non-blocking)
        mlflow_service.log_prediction(
            predicted_class=prediction["class"],
            display_name=prediction["display_name"],
            confidence=prediction["confidence"],
            all_predictions=prediction["all_predictions"],
            model_type=prediction["model_type"],
        )

        disease_info = PLANT_DISEASE_KNOWLEDGE.get(prediction["class"], {})

        return PredictionResponse(
            class_name=prediction["class"],
            display_name=prediction["display_name"],
            confidence=prediction["confidence"],
            all_predictions=prediction["all_predictions"],
            disease_info=disease_info,
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.exception("Prediction failed")
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")
