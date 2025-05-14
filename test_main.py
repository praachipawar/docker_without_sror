from fastapi.testclient import TestClient
from app.main import app          # import your FastAPI instance
from main import app      # import directly from main.py

client = TestClient(app)

def test_root():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}
