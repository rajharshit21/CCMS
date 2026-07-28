from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.services import DocumentService

router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)


@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    """
    Upload a complaint document.

    Returns:
        {
            "document_id": int,
            "filename": str,
            "message": str
        }
    """
    return await DocumentService.upload(
        db=db,
        file=file,
    )


@router.get("/{document_id}")
def get_document(
    document_id: int,
    db: Session = Depends(get_db),
):
    """
    Retrieve uploaded document details.
    """
    return DocumentService.get_document(
        db=db,
        document_id=document_id,
    )