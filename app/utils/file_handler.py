from pathlib import Path
from uuid import uuid4

from fastapi import UploadFile

from app.core.config import settings


UPLOAD_DIR = Path(settings.UPLOAD_DIRECTORY)
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


class FileHandler:
    @staticmethod
    async def save(file: UploadFile) -> tuple[str, str]:
        """
        Save an uploaded file and return its original filename
        and stored file path.
        """

        filename = f"{uuid4()}_{file.filename}"
        filepath = UPLOAD_DIR / filename

        with open(filepath, "wb") as buffer:
            buffer.write(await file.read())

        return file.filename, str(filepath)

    @staticmethod
    def delete(filepath: str) -> bool:
        """
        Delete a file if it exists.
        """

        path = Path(filepath)

        if path.exists():
            path.unlink()
            return True

        return False

    @staticmethod
    def exists(filepath: str) -> bool:
        """
        Check whether a file exists.
        """

        return Path(filepath).exists()