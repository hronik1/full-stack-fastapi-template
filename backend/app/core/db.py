from sqlmodel import SQLModel, create_engine

from app import models  # noqa: F401 — register tables on SQLModel.metadata
from app.core.config import settings

engine = create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False})


def init_db() -> None:
    # No migrations in timeboxed builds: create tables on startup.
    SQLModel.metadata.create_all(engine)
