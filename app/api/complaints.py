from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.complaint import (
    ComplaintCreate,
    ComplaintResponse,
    ComplaintUpdate,
)
from app.services import ComplaintService

router = APIRouter(
    prefix="/complaints",
    tags=["Complaints"],
)


@router.post("/", response_model=ComplaintResponse)
def create_complaint(
    complaint: ComplaintCreate,
    db: Session = Depends(get_db),
):
    return ComplaintService.create(db, complaint)


@router.get("/{complaint_id}", response_model=ComplaintResponse)
def get_complaint(
    complaint_id: int,
    db: Session = Depends(get_db),
):
    complaint = ComplaintService.get(db, complaint_id)

    if complaint is None:
        raise HTTPException(
            status_code=404,
            detail="Complaint not found",
        )

    return complaint


@router.get("/", response_model=list[ComplaintResponse])
def get_all_complaints(
    db: Session = Depends(get_db),
):
    return ComplaintService.get_all(db)


@router.put("/{complaint_id}", response_model=ComplaintResponse)
def update_complaint(
    complaint_id: int,
    complaint: ComplaintUpdate,
    db: Session = Depends(get_db),
):
    updated = ComplaintService.update(
        db,
        complaint_id,
        complaint,
    )

    if updated is None:
        raise HTTPException(
            status_code=404,
            detail="Complaint not found",
        )

    return updated


@router.delete("/{complaint_id}")
def delete_complaint(
    complaint_id: int,
    db: Session = Depends(get_db),
):
    deleted = ComplaintService.delete(
        db,
        complaint_id,
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Complaint not found",
        )

    return {"message": "Complaint deleted successfully"}