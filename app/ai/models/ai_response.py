from typing import List, Optional

from pydantic import BaseModel

from app.ai.models.complaint import AIComplaint


class AIResponse(BaseModel):
    complaint: AIComplaint

    severity: Optional[str] = None
    priority: Optional[str] = None

    initial_assessment: Optional[str] = None

    recommendations: List[str] = []

    message: Optional[str] = None

    status: str = "Completed"