from datetime import date

from app.ai.tools.complaint_extractor import extract_complaint
from app.graph.state import ComplaintState


def extract_complaint_node(state: ComplaintState) -> ComplaintState:
    """
    Extract complaint details from the latest customer message.
    """

    message = state["messages"][-1]

    complaint = extract_complaint(message)

    # System-generated field (not AI-generated)
    complaint.date_received = date.today().isoformat()

    state["complaint"] = complaint

    return state