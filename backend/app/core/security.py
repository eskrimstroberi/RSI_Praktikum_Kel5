from typing import Any
from datetime import datetime, timedelta, UTC
from enum import Enum

import jwt
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

from fastapi import Depends, HTTPException, Request, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.core.config import settings
from app.models.enums import RoleName
from app.models.account import Account
from app.db.session import get_session

ph = PasswordHasher()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/login")


def hash_password(password: str) -> str:
    return ph.hash(password)


def verify_password(hashed_password: str, plain_password: str) -> bool:
    try:
        return ph.verify(hashed_password, plain_password)
    except VerifyMismatchError:
        return False


def create_access_token(data: dict[str, Any]):
    to_encode = data.copy()
    expire = datetime.now(UTC) + timedelta(days=7)
    to_encode.update({"exp": int(expire.timestamp())})
    return jwt.encode(
        to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM
    )


def get_current_user(
    request: Request,
    db: Session = Depends(get_session),
) -> int:
    token_cookie = request.cookies.get("access_token")

    if not token_cookie:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token missing. Please log in.",
        )

    try:
        token = token_cookie.replace("Bearer ", "")
        payload = jwt.decode(
            token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM]
        )
        user_id: str | None = payload.get("sub")

        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token payload")

        return int(user_id)

    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")


def get_current_user_role(
    db: Session = Depends(get_session), account_id: int = Depends(get_current_user)
) -> str:
    account = db.get(Account, account_id)
    if not account or not account.role:
        raise HTTPException(status_code=404, detail="User or Role not found")

    return account.role.name


class RoleChecker:
    def __init__(self, allowed_roles: list[RoleName]):
        self.allowed_roles = allowed_roles

    def __call__(self, user_role: str = Depends(get_current_user_role)):
        if user_role not in self.allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Access denied. Required: {self.allowed_roles}",
            )
        return True


ALLOW_ADMIN = RoleChecker(allowed_roles=RoleName.get_hierarchy(RoleName.ADMIN))
ALLOW_USER = RoleChecker(allowed_roles=RoleName.get_hierarchy(RoleName.USER))
