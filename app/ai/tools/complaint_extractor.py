from app.ai.client.groq_client import GroqClient
from app.ai.models.complaint import AIComplaint
from app.ai.parsers.complaint_parser import parse_complaint
from app.ai.prompts.complaint_prompt import build_complaint_prompt


def extract_complaint(message: str) -> AIComplaint:
    """
    Extract structured complaint information from a customer message.
    """

    prompt = build_complaint_prompt(message)

    client = GroqClient()

    response = client.generate(prompt)

    return parse_complaint(response)