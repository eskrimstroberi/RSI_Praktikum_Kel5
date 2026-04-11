from fastapi.routing import APIRouter
from app.api.v1.endpoints import account, log, registration, role, user, event

api_router = APIRouter()

api_router.include_router(account.router, prefix="/account", tags=["Account"])
api_router.include_router(log.router, prefix="/log", tags=["Log"])
api_router.include_router(registration.router, prefix="/registration", tags=["Registration"])
api_router.include_router(role.router, prefix="/role", tags=["Role"])
api_router.include_router(user.router, prefix="/user", tags=["User"])
api_router.include_router(event.router, prefix="/event", tags=["Event"])