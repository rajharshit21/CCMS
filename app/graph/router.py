from app.graph.state import ComplaintState


def route_request(state: ComplaintState) -> str:
    """
    Determine which workflow path to execute.
    """

    if state["uploaded_documents"]:
        return "document_extraction"

    if state["complaint"] is None:
        return "extract_complaint"

    return "edit_complaint"