import time

import jwt
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

from app.core.config import settings
from app.db.session import SessionLocal
from app.models.log import Log as LogModel


def calculate_duration(start_time: float) -> float:
    return (time.time() - start_time) * 1000


def get_client_ip(request: Request) -> str:
    forwarded = request.headers.get("X-Forwarded-For")
    if forwarded:
        return forwarded.split(",")[0].strip()
    if request.client:
        return request.client.host
    return ""


def get_account_id_from_request(request: Request) -> int | None:
    token_cookie = request.cookies.get("access_token")
    if not token_cookie:
        return None
    try:
        token = token_cookie.replace("Bearer ", "")
        payload = jwt.decode(
            token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM]
        )
        return int(payload.get("sub"))
    except Exception:
        return None


def derive_entity(path: str) -> str:
    if path.startswith("/api/v1/account"):
        return "Account"
    if path.startswith("/api/v1/event"):
        return "Event"
    if path.startswith("/api/v1/registration"):
        return "Registration"
    if path.startswith("/api/v1/role"):
        return "Role"
    if path.startswith("/api/v1/user"):
        return "User"
    if path.startswith("/api/v1/log"):
        return "Log"
    return ""


def get_action(method: str, path: str) -> str:
    if path.endswith("/login"):
        return "LOGIN"
    if path.endswith("/logout"):
        return "LOGOUT"
    mapping = {
        "GET": "READ",
        "POST": "CREATE",
        "PUT": "UPDATE",
        "PATCH": "PATCH",
        "DELETE": "DELETE",
    }
    return mapping.get(method, method)


class AuditMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()

        request.state.audit_entity = None
        request.state.audit_entity_id = None
        request.state.audit_account_id = None

        response = await call_next(request)

        duration_ms = calculate_duration(start_time)
        path = str(request.url.path)
        ip_address = get_client_ip(request)
        user_agent = request.headers.get("user-agent") or ""

        account_id = (
            request.state.audit_account_id or get_account_id_from_request(request)
        )
        entity = request.state.audit_entity or derive_entity(path)
        entity_id = request.state.audit_entity_id

        if path == "/" or path.startswith("/docs") or path.startswith("/openapi"):
            return response

        try:
            db = SessionLocal()
            log_entry = LogModel(
                account_id=account_id,
                action=get_action(request.method, path),
                endpoint=path,
                method=request.method,
                response_status=response.status_code,
                duration_ms=round(duration_ms, 2),
                ip_address=ip_address,
                user_agent=user_agent,
                entity=entity,
                entity_id=entity_id,
            )
            db.add(log_entry)
            db.commit()
        except Exception:
            pass
        finally:
            db.close()

        return response
