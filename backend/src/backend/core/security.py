from typing import Any
from datetime import datetime, timedelta, UTC
from jose import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from backend.core.config import settings
from backend.db.session import get_db
from backend.models.account import Account

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/login")


def create_access_token(data: dict[str, Any]):
    to_encode = data.copy()
    expire = datetime.now(UTC) + timedelta(days=7)
    to_encode.update({"exp": int(expire.timestamp())})
    return jwt.encode(
        to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM
    )


def get_current_user(
    db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)
) -> int:
    try:
        payload = jwt.decode(
            token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM]
        )
        user_id: str | None = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return int(user_id)
    except Exception:
        raise HTTPException(status_code=401, detail="Could not validate credentials")


def get_current_user_role(
    db: Session = Depends(get_db), account_id: int = Depends(get_current_user)
) -> str:
    account = db.get_one(Account, account_id)
    if not account:
        raise HTTPException(status_code=404, detail="User not found")

    # Return the string name of the role (e.g., "Admin", "User")
    return account.role.name


class RoleChecker:
    def __init__(self, allowed_roles: list[str]):
        self.allowed_roles = allowed_roles

    def __call__(self, user_role: str = Depends(get_current_user_role)):
        if user_role not in self.allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Access denied. Required: {self.allowed_roles}",
            )
        return True
