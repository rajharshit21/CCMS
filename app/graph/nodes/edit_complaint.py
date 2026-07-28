from app.ai.tools.complaint_editor import edit_complaint
from app.graph.state import ComplaintState


def edit_complaint_node(state: ComplaintState) -> ComplaintState:
    """
    Update an existing complaint using the latest customer message.
    """

    message = state["messages"][-1]

    updated = edit_complaint(
        complaint=state["complaint"].model_dump(),
        message=message,
    )

    state["complaint"] = updated

    return state