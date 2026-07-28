def build_risk_prompt(
    complaint: dict,
) -> str:
    return f"""
You are a Pharmaceutical Quality Assurance specialist.

Analyse the following complaint.

Complaint:

{complaint}

Determine:

- severity
- priority
- initial_assessment

Severity should be one of:

- Low
- Medium
- High
- Critical

Priority should be one of:

- Low
- Medium
- High
- Critical

Return ONLY valid JSON.

Example:

{{
    "severity": "High",
    "priority": "Critical",
    "initial_assessment": "Possible product contamination requiring immediate investigation."
}}
"""