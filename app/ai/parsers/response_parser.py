import json
import re

from app.ai.models.ai_response import AIResponse
from app.ai.models.complaint import AIComplaint


def parse_ai_response(
    response: str,
) -> AIResponse:
    """
    Parse the complete AI response returned by the LLM.
    """

    response = response.strip()

    # Remove Markdown code fences added by the LLM
    response = re.sub(
        r"^```(?:json)?\s*|\s*```$",
        "",
        response,
        flags=re.IGNORECASE | re.MULTILINE,
    )

    data = json.loads(response)

    complaint = AIComplaint(
        **data.get("complaint", {})
    )

    return AIResponse(
        complaint=complaint,
        severity=data.get("severity"),
        priority=data.get("priority"),
        initial_assessment=data.get("initial_assessment"),
        recommendations=data.get(
            "recommendations",
            [],
        ),
        message=data.get("message"),
        status=data.get(
            "status",
            "Completed",
        ),
    )