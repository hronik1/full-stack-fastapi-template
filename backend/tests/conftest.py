import os
from collections.abc import Generator

import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session, SQLModel, create_engine
from sqlmodel.pool import StaticPool

# Keep the app's startup create_all off the real DB file during tests.
os.environ["APP_DATABASE_URL"] = "sqlite://"

from app.api.deps import get_db  # noqa: E402
from app.main import app  # noqa: E402


@pytest.fixture
def db() -> Generator[Session]:
    # Fresh in-memory DB per test.
    engine = create_engine(
        "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session


@pytest.fixture
def client(db: Session) -> Generator[TestClient]:
    app.dependency_overrides[get_db] = lambda: db
    with TestClient(app) as c:
        yield c
    app.dependency_overrides.clear()
