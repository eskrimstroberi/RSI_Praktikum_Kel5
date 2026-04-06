from fastapi.routing import APIRouter
from backend.api.v1.endpoints import account

api_router = APIRouter()

api_router.include_router(account.router, prefix="/account", tags=["Account"])

