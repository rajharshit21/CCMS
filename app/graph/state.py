from typing import List, Optional, TypedDict

from app.ai.models.complaint import AIComplaint


class ComplaintState(TypedDict):
    messages: List[str]

    complaint: Optional[AIComplaint]

    uploaded_documents: List[str]

    severity: Optional[str]
    priority: Optional[str]

    initial_assessment: Optional[str]

    recommendations: List[str]

    status: str