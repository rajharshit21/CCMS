from datetime import datetime

from sqlalchemy import (
    Column,
    Date,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
)
from sqlalchemy.orm import relationship

from app.database.connection import Base


class Complaint(Base):
    __tablename__ = "complaints"

    id = Column(Integer, primary_key=True, index=True)

    customer_name = Column(String(100), nullable=False)
    email = Column(String(100))
    phone = Column(String(30))

    company = Column(String(100))

    product_name = Column(String(100))
    batch_number = Column(String(50))
    manufacturing_site = Column(String(100))
    manufacturing_date = Column(Date)
    expiry_date = Column(Date)
    pack_size = Column(String(50))

    complaint_type = Column(String(100))
    complaint_description = Column(Text)

    severity = Column(String(50))
    priority = Column(String(50))

    recommended_action = Column(Text)
    initial_assessment = Column(Text)

    status = Column(String(50), default="Draft")

    created_at = Column(DateTime, default=datetime.utcnow)

    documents = relationship(
        "Document",
        back_populates="complaint",
        cascade="all, delete-orphan",
    )

    conversations = relationship(
        "Conversation",
        back_populates="complaint",
        cascade="all, delete-orphan",
    )

    ai_interactions = relationship(
        "AIInteraction",
        back_populates="complaint",
        cascade="all, delete-orphan",
    )


class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)

    complaint_id = Column(
        Integer,
        ForeignKey("complaints.id"),
        nullable=True,          # Required for AI-first workflow
    )

    filename = Column(String(255), nullable=False)
    file_path = Column(String(500), nullable=False)
    file_type = Column(String(50), nullable=False)

    uploaded_at = Column(DateTime, default=datetime.utcnow)

    complaint = relationship(
        "Complaint",
        back_populates="documents",
    )


class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(Integer, primary_key=True, index=True)

    complaint_id = Column(
        Integer,
        ForeignKey("complaints.id"),
        nullable=False,
    )

    role = Column(String(20))
    message = Column(Text)

    timestamp = Column(DateTime, default=datetime.utcnow)

    complaint = relationship(
        "Complaint",
        back_populates="conversations",
    )


class AIInteraction(Base):
    __tablename__ = "ai_interactions"

    id = Column(Integer, primary_key=True, index=True)

    complaint_id = Column(
        Integer,
        ForeignKey("complaints.id"),
        nullable=False,
    )

    prompt = Column(Text)
    response = Column(Text)

    model = Column(String(100))

    created_at = Column(DateTime, default=datetime.utcnow)

    complaint = relationship(
        "Complaint",
        back_populates="ai_interactions",
    )