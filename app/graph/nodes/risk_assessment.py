from app.ai.tools.risk_analyzer import analyze_risk
from app.graph.state import ComplaintState


def risk_assessment_node(state: ComplaintState) -> ComplaintState:
    """
    Analyse complaint severity and priority.
    """

    result = analyze_risk(
        state["complaint"].model_dump()
    )

    state["severity"] = result.severity
    state["priority"] = result.priority
    state["initial_assessment"] = result.initial_assessment

    return state