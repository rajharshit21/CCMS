from datetime import datetime, timedelta

from jose import jwt

from app.core.config import settings


def create_access_token(
    data: dict,
    expires_minutes: int = 60,
):
    payload = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=expires_minutes
    )

    payload["exp"] = expire

    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )