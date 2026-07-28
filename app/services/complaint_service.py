from sqlalchemy.orm import Session

from app.database.crud.complaint_crud import (
    create_complaint,
    delete_complaint,
    get_all_complaints,
    get_complaint_by_id,
    update_complaint,
)
from app.schemas.complaint import (
    ComplaintCreate,
    ComplaintUpdate,
)


class ComplaintService:

    @staticmethod
    def create(db: Session, complaint: ComplaintCreate):
        return create_complaint(db, complaint)

    @staticmethod
    def get(db: Session, complaint_id: int):
        return get_complaint_by_id(db, complaint_id)

    @staticmethod
    def get_all(db: Session):
        return get_all_complaints(db)

    @staticmethod
    def update(
        db: Session,
        complaint_id: int,
        complaint: ComplaintUpdate,
    ):
        return update_complaint(
            db,
            complaint_id,
            complaint,
        )

    @staticmethod
    def delete(
        db: Session,
        complaint_id: int,
    ):
        return delete_complaint(
            db,
            complaint_id,
        )