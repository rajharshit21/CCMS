from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class DocumentBase(BaseModel):
    filename: str
    file_type: str
    file_path: Optional[str] = None


class DocumentCreate(DocumentBase):
    complaint_id: Optional[int] = None


class DocumentResponse(DocumentBase):
    id: int
    complaint_id: Optional[int] = None
    uploaded_at: datetime

    model_config = ConfigDict(from_attributes=True)