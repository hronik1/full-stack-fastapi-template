from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        # Optional top level .env file (one level above ./backend/)
        env_file="../.env",
        # Prefixed so machine-wide vars (e.g. a global DATABASE_URL) can't leak in.
        env_prefix="APP_",
        env_ignore_empty=True,
        extra="ignore",
    )
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "App"
    FRONTEND_HOST: str = "http://localhost:5173"
    FASTAPI_ENV: Literal["development"] | None = None
    # SQLite file in ./backend by default; override with APP_DATABASE_URL.
    DATABASE_URL: str = "sqlite:///./app.db"


settings = Settings()
