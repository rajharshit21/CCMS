import json
import re

from app.ai.models.complaint import AIComplaint


def parse_complaint(response: str) -> AIComplaint:
    """
    Parse the complaint JSON returned by the LLM.
    """

    response = response.strip()

    response = re.sub(
        r"^```(?:json)?\s*|\s*```$",
        "",
        response,
        flags=re.IGNORECASE | re.MULTILINE,
    )

    data = json.loads(response)

    return AIComplaint(**data)