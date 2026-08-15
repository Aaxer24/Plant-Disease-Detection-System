"""Chat endpoint."""

import logging

from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse

from src.plant_api.dependencies import get_chat_service
from src.plant_api.schemas.api_schemas import ChatRequest, ChatResponse
from src.plant_api.services.chat_service import ChatService

logger = logging.getLogger(__name__)

router = APIRouter(tags=["chat"])


@router.post("/chat", response_model=ChatResponse)
async def chat_with_ai(
    request: ChatRequest,
    chat_service: ChatService = Depends(get_chat_service),
):
    """Chat with AI about plant diseases."""
    return await chat_service.chat(request)


@router.post("/chat/stream")
async def chat_with_ai_stream(
    request: ChatRequest,
    chat_service: ChatService = Depends(get_chat_service),
):
    """Chat with AI about plant diseases, streaming the reply token-by-token."""
    return StreamingResponse(chat_service.stream_chat(request), media_type="text/plain")
