from pathlib import Path
from uuid import uuid4

from fastapi import UploadFile
from sqlalchemy.orm import Session

from app.database.crud.document_crud import (
    create_document,
    delete_document,
    get_document_by_id,
)
from app.schemas.document import DocumentCreate


UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


class DocumentService:

    @staticmethod
    async def upload(
        db: Session,
        file: UploadFile,
    ):
        filename = f"{uuid4()}_{file.filename}"
        filepath = UPLOAD_DIR / filename

        with open(filepath, "wb") as buffer:
            buffer.write(await file.read())

        document = DocumentCreate(
            complaint_id=None,          # Will be linked after AI creates the complaint
            filename=file.filename,
            file_path=str(filepath),
            file_type=file.content_type,
        )

        saved_document = create_document(
            db=db,
            document_data=document.model_dump(),   # ✅ Convert Pydantic model to dict
        )

        return {
            "document_id": saved_document.id,
            "filename": saved_document.filename,
            "file_type": saved_document.file_type,
            "message": "Document uploaded successfully.",
        }

    @staticmethod
    def get(
        db: Session,
        document_id: int,
    ):
        return get_document_by_id(
            db,
            document_id,
        )

    @staticmethod
    def delete(
        db: Session,
        document_id: int,
    ):
        document = get_document_by_id(
            db,
            document_id,
        )

        if document:
            path = Path(document.file_path)

            if path.exists():
                path.unlink()

        return delete_document(
            db,
            document_id,
        )