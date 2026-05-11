from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.main import api_router
from app.core.config import Settings

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[Settings.FRONTEND_URL],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api/v1")


@app.get("/")
def home():
    return "Welcome"