import pytest

from fastapi.testclient import TestClient
from src.api.server.fast import app

@pytest.fixture
def client(filled_db):
    app.state.db = filled_db
    with TestClient(app) as c:
        yield c
