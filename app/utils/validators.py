from fastapi import HTTPException, UploadFile

from app.core.constants import ALLOWED_FILE_TYPES
from app.core.config import settings


def validate_file_type(file: UploadFile) -> None:
    """
    Validate uploaded file type.
    """

    if file.content_type not in ALLOWED_FILE_TYPES:
        raise HTTPException(
            status_code=400,
            detail="Unsupported file type.",
        )


async def validate_file_size(file: UploadFile) -> None:
    """
    Validate uploaded file size.
    """

    content = await file.read()

    if len(content) > settings.MAX_UPLOAD_SIZE:
        raise HTTPException(
            status_code=400,
            detail="File exceeds maximum upload size.",
        )

    await file.seek(0)


def validate_severity(value: str) -> str:
    """
    Validate complaint severity.
    """

    allowed = {
        "Low",
        "Medium",
        "High",
        "Critical",
    }

    if value not in allowed:
        raise ValueError(
            f"Invalid severity: {value}"
        )

    return value


def validate_priority(value: str) -> str:
    """
    Validate complaint priority.
    """

    allowed = {
        "Low",
        "Medium",
        "High",
        "Critical",
    }

    if value not in allowed:
        raise ValueError(
            f"Invalid priority: {value}"
        )

    return value