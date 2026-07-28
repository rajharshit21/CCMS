from sqlalchemy.orm import Session

from app.database.models import Complaint
from app.schemas.complaint import (
    ComplaintCreate,
    ComplaintUpdate,
)


def create_complaint(
    db: Session,
    complaint: ComplaintCreate,
):
    # Convert Pydantic model to dictionary
    complaint_data = complaint.model_dump(exclude_none=True)

    db_complaint = Complaint(**complaint_data)

    db.add(db_complaint)
    db.commit()
    db.refresh(db_complaint)

    return db_complaint


def get_complaint_by_id(
    db: Session,
    complaint_id: int,
):
    return (
        db.query(Complaint)
        .filter(Complaint.id == complaint_id)
        .first()
    )


def get_all_complaints(
    db: Session,
):
    return (
        db.query(Complaint)
        .order_by(Complaint.created_at.desc())
        .all()
    )


def update_complaint(
    db: Session,
    complaint_id: int,
    complaint: ComplaintUpdate,
):
    db_complaint = get_complaint_by_id(
        db,
        complaint_id,
    )

    if db_complaint is None:
        return None

    update_data = complaint.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():
        setattr(db_complaint, key, value)

    db.commit()
    db.refresh(db_complaint)

    return db_complaint


def delete_complaint(
    db: Session,
    complaint_id: int,
):
    db_complaint = get_complaint_by_id(
        db,
        complaint_id,
    )

    if db_complaint is None:
        return False

    db.delete(db_complaint)
    db.commit()

    return True