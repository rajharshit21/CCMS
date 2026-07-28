from app.graph.state import ComplaintState

from pprint import pprint

def response_node(state: ComplaintState) -> ComplaintState:
    print("\n===== FINAL STATE =====")
    pprint(state)
    print("=======================\n")

    complaint = state["complaint"]

    complaint.severity = state["severity"]
    complaint.priority = state["priority"]
    complaint.initial_assessment = state["initial_assessment"]

    if state["recommendations"]:
        complaint.recommended_action = "\n".join(state["recommendations"])

    state["status"] = "Completed"

    return state