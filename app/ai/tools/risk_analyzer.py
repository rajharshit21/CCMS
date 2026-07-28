from app.ai.client.groq_client import GroqClient
from app.ai.parsers.response_parser import parse_ai_response
from app.ai.prompts.risk_prompt import build_risk_prompt


def analyze_risk(
    complaint: dict,
):
    """
    Analyse complaint severity and priority.
    """

    prompt = build_risk_prompt(complaint)

    client = GroqClient()

    response = client.generate(prompt)

    return parse_ai_response(response)