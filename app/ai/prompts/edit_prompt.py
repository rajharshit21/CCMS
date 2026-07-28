def build_edit_prompt(
    complaint: dict,
    message: str,
) -> str:
    return f"""
You are editing an existing pharmaceutical complaint.

Current Complaint:

{complaint}

Customer Update:

{message}

Update only the affected fields.

Do not remove existing information unless the customer explicitly corrects it.

Return ONLY the updated complaint as valid JSON.

Do not include explanations.

Do not wrap the JSON inside markdown.
"""