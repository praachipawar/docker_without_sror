from fastapi import FastAPI
from app.main import app

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI"}