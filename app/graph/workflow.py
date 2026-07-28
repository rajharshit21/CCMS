from langgraph.graph import END, StateGraph

from app.graph.router import route_request
from app.graph.state import ComplaintState

from app.graph.nodes.edit_complaint import edit_complaint_node
from app.graph.nodes.extract_complaint import extract_complaint_node
from app.graph.nodes.recommendation import recommendation_node
from app.graph.nodes.response import response_node
from app.graph.nodes.risk_assessment import risk_assessment_node


workflow = StateGraph(ComplaintState)

workflow.add_node(
    "extract_complaint",
    extract_complaint_node,
)

workflow.add_node(
    "edit_complaint",
    edit_complaint_node,
)

workflow.add_node(
    "risk_assessment",
    risk_assessment_node,
)

workflow.add_node(
    "recommendation",
    recommendation_node,
)

workflow.add_node(
    "response",
    response_node,
)

workflow.set_conditional_entry_point(
    route_request,
    {
        "extract_complaint": "extract_complaint",
        "edit_complaint": "edit_complaint",
    },
)

workflow.add_edge(
    "extract_complaint",
    "risk_assessment",
)

workflow.add_edge(
    "edit_complaint",
    "risk_assessment",
)

workflow.add_edge(
    "risk_assessment",
    "recommendation",
)

workflow.add_edge(
    "recommendation",
    "response",
)

workflow.add_edge(
    "response",
    END,
)

complaint_graph = workflow.compile()