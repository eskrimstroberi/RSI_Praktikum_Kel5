from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from app.core.security import ALLOW_ADMIN, ALLOW_USER
from app.db.session import get_session
from app.schemas.user import UserCreate, UserUpdate, UserResponse
from app.services.user import UserService

router = APIRouter()


def get_user_service(session: Session = Depends(get_session)):
    return UserService(session)


# ✅ hanya Admin + SuperAdmin boleh lihat semua user
@router.get("/", response_model=list[UserResponse], status_code=status.HTTP_200_OK)
def get_users(
    service: UserService = Depends(get_user_service)
):
    return service.get_all()


# ✅ semua role boleh lihat detail user
@router.get("/{user_id}", response_model=UserResponse, status_code=status.HTTP_200_OK)
def get_user(
    user_id: int,
    service: UserService = Depends(get_user_service)
):
    user = service.get_by_id(user_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return user


# 🔒 hanya SuperAdmin boleh create user
@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(
    data: UserCreate,
    service: UserService = Depends(get_user_service)
):
    return service.create(data)


# 🔒 hanya SuperAdmin boleh update user
@router.put("/{user_id}", response_model=UserResponse, status_code=status.HTTP_200_OK)
def update_user(
    user_id: int,
    data: UserUpdate,
    service: UserService = Depends(get_user_service)
):
    user = service.update_user(user_id, data)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return user


# 🔒 hanya ADMIN boleh delete user
@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(
    user_id: int,
    service: UserService = Depends(get_user_service)
):
    deleted = service.delete(user_id)

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return None