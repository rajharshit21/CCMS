def build_complaint_prompt(message: str) -> str:
    return f"""
You are an AI assistant for a Pharmaceutical Customer Complaint Management System.

Your task is to extract structured complaint information from the customer's message.

Return ONLY valid JSON.

Rules:

- If information is missing, return null.
- Manufacturing and expiry dates should be returned exactly as mentioned.
- Date received should be today's complaint date if words like "today", "today morning", "today afternoon", etc. are used.
- Complaint Origin refers to how or from where the complaint was received.

Examples:

- Email
- Phone
- Customer Portal
- Sales Representative
- Regulatory Authority
- Other

If none of the above are explicitly mentioned, infer the closest option.

Return this JSON exactly:

{{
    "complaint_origin": null,
    "date_received": null,

    "customer_name": null,
    "email": null,
    "phone": null,
    "company": null,

    "product_name": null,
    "batch_number": null,
    "manufacturing_site": null,
    "manufacturing_date": null,
    "expiry_date": null,
    "pack_size": null,

    "complaint_type": null,
    "complaint_description": null,

    "severity": null,
    "priority": null,

    "recommended_action": null,
    "initial_assessment": null
}}

Customer Message:

{message}

Return ONLY valid JSON.
"""