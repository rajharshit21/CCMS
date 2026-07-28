from fastapi import APIRouter

from .chat import router as chat_router
from .complaints import router as complaints_router
from .documents import router as documents_router
from .health import router as health_router

api_router = APIRouter()

api_router.include_router(health_router)
api_router.include_router(chat_router)
api_router.include_router(complaints_router)
api_router.include_router(documents_router)

__all__ = [
    "api_router",
]