from typing import Optional

from pydantic import BaseModel

from app.schemas.complaint import ComplaintResponse


class ChatRequest(BaseModel):
    message: str
    complaint_id: Optional[int] = None


class ChatMessage(BaseModel):
    role: str
    message: str


class ChatResponse(BaseModel):
    reply: str
    complaint: ComplaintResponse
    status: str