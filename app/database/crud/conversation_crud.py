from typing import Optional

from sqlalchemy.orm import Session

from app.database.models import Conversation


def create_conversation(
    db: Session,
    conversation_data: dict,
) -> Conversation:
    """
    Create a new conversation message.
    """
    conversation = Conversation(**conversation_data)

    db.add(conversation)
    db.commit()
    db.refresh(conversation)

    return conversation


def get_conversation_by_id(
    db: Session,
    conversation_id: int,
) -> Optional[Conversation]:
    """
    Retrieve a conversation message by its ID.
    """
    return (
        db.query(Conversation)
        .filter(Conversation.id == conversation_id)
        .first()
    )


def get_conversations_by_complaint(
    db: Session,
    complaint_id: int,
) -> list[Conversation]:
    """
    Retrieve all conversation messages for a complaint.
    """
    return (
        db.query(Conversation)
        .filter(Conversation.complaint_id == complaint_id)
        .order_by(Conversation.timestamp.asc())
        .all()
    )


def delete_conversation(
    db: Session,
    conversation_id: int,
) -> bool:
    """
    Delete a conversation message.
    """
    conversation = get_conversation_by_id(db, conversation_id)

    if conversation is None:
        return False

    db.delete(conversation)
    db.commit()

    return True