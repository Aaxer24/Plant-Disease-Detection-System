"""Pydantic v2 request and response schemas."""

from typing import Optional

from pydantic import BaseModel


class ChatMessage(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    message: str
    conversation_history: list[ChatMessage] = []
    disease_context: Optional[str] = None
    confidence: Optional[float] = None


class ChatResponse(BaseModel):
    response: str
    disease_context: Optional[str] = None


class PredictionResponse(BaseModel):
    class_name: str
    display_name: str
    confidence: float
    all_predictions: dict
    disease_info: dict


class HealthResponse(BaseModel):
    status: str
    model_loaded: bool
    version: str
