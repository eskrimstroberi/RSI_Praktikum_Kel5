from fastapi import FastAPI
from backend.api.v1.main import api_router

app = FastAPI()

app.include_router(api_router, prefix="/api/v1")


@app.get("/")
def home():
    return "Welcome"
