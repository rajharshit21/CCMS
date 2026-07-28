from typing import Optional

from pydantic import BaseModel


class RiskAssessment(BaseModel):
    severity: Optional[str] = None
    priority: Optional[str] = None
    initial_assessment: Optional[str] = None
    recommended_action: Optional[str] = None