from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "Customer Complaint Management System"
    APP_VERSION: str = "1.0.0"

    API_PREFIX: str = "/api"

    DATABASE_URL: str

    GROQ_API_KEY: str
    GROQ_MODEL: str = "llama-3.3-70b-versatile"

    SECRET_KEY: str
    ALGORITHM: str = "HS256"

    UPLOAD_DIRECTORY: str = "uploads"

    MAX_UPLOAD_SIZE: int = 10 * 1024 * 1024

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
    )


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()