from app.ai.client.groq_client import GroqClient
from app.ai.models.complaint import AIComplaint
from app.ai.parsers.complaint_parser import parse_complaint
from app.ai.prompts.edit_prompt import build_edit_prompt


def edit_complaint(
    complaint: dict,
    message: str,
) -> AIComplaint:
    """
    Update an existing complaint using new customer information.
    """

    prompt = build_edit_prompt(
        complaint=complaint,
        message=message,
    )

    client = GroqClient()

    response = client.generate(prompt)

    return parse_complaint(response)