from fastapi.testclient import TestClient
from main import app  # Correct import

client = TestClient(app)

def test_root():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json() == {"message": "Hello from FastAPI"}  # Update this to match the actual response