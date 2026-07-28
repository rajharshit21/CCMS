from typing import Optional

from sqlalchemy.orm import Session

from app.database.models import Document


def create_document(
    db: Session,
    document_data: dict,
) -> Document:
    """
    Save a document record.
    """
    document = Document(**document_data)

    db.add(document)
    db.commit()
    db.refresh(document)

    return document


def get_document_by_id(
    db: Session,
    document_id: int,
) -> Optional[Document]:
    """
    Retrieve a document by its ID.
    """
    return (
        db.query(Document)
        .filter(Document.id == document_id)
        .first()
    )


def get_documents_by_complaint(
    db: Session,
    complaint_id: int,
) -> list[Document]:
    """
    Retrieve all documents belonging to a complaint.
    """
    return (
        db.query(Document)
        .filter(Document.complaint_id == complaint_id)
        .all()
    )


def delete_document(
    db: Session,
    document_id: int,
) -> bool:
    """
    Delete a document record.
    """
    document = get_document_by_id(db, document_id)

    if document is None:
        return False

    db.delete(document)
    db.commit()

    return True