from fastapi import Depends
from sqlmodel import Session
import backend.repositories.user as user_repo
import backend.schemas.user as user_schema
from backend.models.user import User as UserModel


def get(db: Session):
    return user_repo.get_all(db)


def get_all(db: Session, user_id: int):
    return user_repo.get_by_id(db, user_id)


def create(db: Session, user_data: user_schema.UserCreate):
    user = UserModel(
        first_name=user_data.first_name,
        last_name=user_data.last_name,
        whatsapp=user_data.whatsapp,
    )
    return user_repo.create(db, user)


def update(db: Session, user_id: int, user_data: user_schema.UserUpdate):
    user = UserModel(
        first_name=user_data.first_name,
        last_name=user_data.last_name,
        whatsapp=user_data.whatsapp,
    )
    res = user_repo.update(db, user_id, user)


def delete(db: Session, user_id: int):
    user = user_repo.get_by_id(db, user_id)
    res = user_repo.delete(db, user)
    return res

