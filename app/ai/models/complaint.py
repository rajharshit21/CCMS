from typing import Optional

from pydantic import BaseModel


class AIComplaint(BaseModel):

    # Complaint Origin
    complaint_origin: Optional[str] = None
    date_received: Optional[str] = None

    # Customer
    customer_name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    company: Optional[str] = None

    # Product
    product_name: Optional[str] = None
    batch_number: Optional[str] = None
    manufacturing_site: Optional[str] = None
    manufacturing_date: Optional[str] = None
    expiry_date: Optional[str] = None
    pack_size: Optional[str] = None

    # Complaint
    complaint_type: Optional[str] = None
    complaint_description: Optional[str] = None

    # Assessment
    severity: Optional[str] = None
    priority: Optional[str] = None

    recommended_action: Optional[str] = None
    initial_assessment: Optional[str] = None