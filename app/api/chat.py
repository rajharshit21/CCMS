from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.chat import ChatRequest
from app.services import ChatService

router = APIRouter(
    prefix="/chat",
    tags=["AI Chat"],
)


@router.post("")
def chat(
    request: ChatRequest,
    db: Session = Depends(get_db),
):
    return ChatService.process_message(
        db=db,
        request=request,
    )