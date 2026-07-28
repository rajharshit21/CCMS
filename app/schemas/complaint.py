from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class ComplaintBase(BaseModel):
    customer_name: str
    email: Optional[str] = None
    phone: Optional[str] = None

    company: Optional[str] = None

    product_name: Optional[str] = None
    batch_number: Optional[str] = None
    manufacturing_site: Optional[str] = None
    manufacturing_date: Optional[date] = None
    expiry_date: Optional[date] = None
    pack_size: Optional[str] = None

    complaint_type: Optional[str] = None
    complaint_description: Optional[str] = None

    severity: Optional[str] = None
    priority: Optional[str] = None

    recommended_action: Optional[str] = None
    initial_assessment: Optional[str] = None


class ComplaintCreate(ComplaintBase):
    """
    Schema used when creating a complaint.
    """
    pass


class ComplaintUpdate(BaseModel):
    customer_name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None

    company: Optional[str] = None

    product_name: Optional[str] = None
    batch_number: Optional[str] = None
    manufacturing_site: Optional[str] = None
    manufacturing_date: Optional[date] = None
    expiry_date: Optional[date] = None
    pack_size: Optional[str] = None

    complaint_type: Optional[str] = None
    complaint_description: Optional[str] = None

    severity: Optional[str] = None
    priority: Optional[str] = None

    recommended_action: Optional[str] = None
    initial_assessment: Optional[str] = None

    status: Optional[str] = None


class ComplaintResponse(ComplaintBase):
    id: int
    status: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)