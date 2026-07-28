from app.ai.client.groq_client import GroqClient
from app.ai.parsers.response_parser import parse_ai_response
from app.ai.prompts.recommendation_prompt import (
    build_recommendation_prompt,
)


def generate_recommendations(
    complaint: dict,
):
    """
    Generate recommended actions for a complaint.
    """

    prompt = build_recommendation_prompt(complaint)

    client = GroqClient()

    response = client.generate(prompt)

    return parse_ai_response(response)