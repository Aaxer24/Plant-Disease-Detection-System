"""FastAPI application factory."""

import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.plant_api import __version__
from src.plant_api.config import get_settings
from src.plant_api.dependencies import get_mlflow_service, get_model_service
from src.plant_api.routers import chat, health, predict

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage application startup and shutdown."""
    settings = get_settings()
    logging.basicConfig(
        level=getattr(logging, settings.LOG_LEVEL.upper(), logging.INFO),
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )
    logger.info("Starting Plant Disease Detection API v%s", __version__)

    # Eagerly initialise singletons so model loads at startup
    get_model_service()
    get_mlflow_service()

    logger.info("Startup complete — API ready")
    yield
    logger.info("Shutting down")


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    settings = get_settings()

    app = FastAPI(
        title="Plant Disease Detection API",
        description=(
            "AI-powered plant disease detection for potato, tomato and pepper crops, "
            "with MLflow tracking and a RAG chatbot"
        ),
        version=__version__,
        lifespan=lifespan,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(health.router)
    app.include_router(predict.router)
    app.include_router(chat.router)

    return app


app = create_app()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("src.plant_api.main:app", host="0.0.0.0", port=8000, reload=True)
