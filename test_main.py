from fastapi.testclient import TestClient
from main import app
from docker_without_sror.main import app      # import directly from main.py

client = TestClient(app)

def test_root():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}
