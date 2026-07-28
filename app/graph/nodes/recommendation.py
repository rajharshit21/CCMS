from app.ai.tools.recommendation_generator import (
    generate_recommendations,
)
from app.graph.state import ComplaintState


def recommendation_node(state: ComplaintState) -> ComplaintState:
    """
    Generate recommendations for the complaint.
    """

    result = generate_recommendations(
        state["complaint"].model_dump()
    )

    state["recommendations"] = result.recommendations

    return state