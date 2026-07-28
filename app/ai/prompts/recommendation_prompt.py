def build_recommendation_prompt(
    complaint: dict,
) -> str:
    return f"""
You are a Pharmaceutical Quality Assurance expert.

Based on the complaint below, recommend appropriate actions.

Complaint:

{complaint}

Generate practical recommendations for investigation and resolution.

Return ONLY valid JSON.

Example:

{{
    "recommendations": [
        "Quarantine the affected batch.",
        "Notify the Quality Assurance department.",
        "Initiate root cause investigation.",
        "Review manufacturing records."
    ]
}}
"""