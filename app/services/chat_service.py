from sqlalchemy.orm import Session

from app.database.crud.ai_interaction_crud import (
    create_ai_interaction,
)
from app.database.crud.conversation_crud import (
    create_conversation,
)
from app.graph.workflow import complaint_graph
from app.graph.state import ComplaintState
from app.schemas.chat import ChatRequest


class ChatService:

    @staticmethod
    def process_message(
        db: Session,
        request: ChatRequest,
    ):
        state: ComplaintState = {
            "messages": [request.message],
            "complaint": None,
            "uploaded_documents": [],
            "severity": None,
            "priority": None,
            "initial_assessment": None,
            "recommendations": [],
            "status": "Processing",
        }

        result = complaint_graph.invoke(state)

        if request.complaint_id:

            create_conversation(
                db=db,
                complaint_id=request.complaint_id,
                role="user",
                message=request.message,
            )

            create_ai_interaction(
                db=db,
                complaint_id=request.complaint_id,
                prompt=request.message,
                response=result["status"],
                model="Groq",
            )

        return result