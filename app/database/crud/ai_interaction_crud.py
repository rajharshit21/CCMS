from typing import Optional

from sqlalchemy.orm import Session

from app.database.models import AIInteraction


def create_ai_interaction(
    db: Session,
    interaction_data: dict,
) -> AIInteraction:
    """
    Save an AI interaction.
    """
    interaction = AIInteraction(**interaction_data)

    db.add(interaction)
    db.commit()
    db.refresh(interaction)

    return interaction


def get_ai_interaction_by_id(
    db: Session,
    interaction_id: int,
) -> Optional[AIInteraction]:
    """
    Retrieve an AI interaction by its ID.
    """
    return (
        db.query(AIInteraction)
        .filter(AIInteraction.id == interaction_id)
        .first()
    )


def get_ai_interactions_by_complaint(
    db: Session,
    complaint_id: int,
) -> list[AIInteraction]:
    """
    Retrieve all AI interactions for a complaint.
    """
    return (
        db.query(AIInteraction)
        .filter(AIInteraction.complaint_id == complaint_id)
        .order_by(AIInteraction.created_at.asc())
        .all()
    )


def delete_ai_interaction(
    db: Session,
    interaction_id: int,
) -> bool:
    """
    Delete an AI interaction.
    """
    interaction = get_ai_interaction_by_id(db, interaction_id)

    if interaction is None:
        return False

    db.delete(interaction)
    db.commit()

    return True