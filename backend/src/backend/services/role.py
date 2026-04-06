from sqlmodel import Session
from fastapi import HTTPException
import backend.repositories.role as role_repo
import backend.schemas.role as role_schema
from backend.models.role import Role as RoleModel


def create(db: Session, role=role_schema.RoleCreate):
    role_model = RoleModel(name=role.name)
    return role_repo.create(db, role_model)


def get_all(db: Session):
    return role_repo.get_all(db)


def get_by_id(db: Session, role_id: int):
    role = role_repo.get_by_id(db, role_id)
    if not role:
        raise HTTPException(404, "Role not found")
    return role


def delete(db: Session, role_id: int):
    role_model = role_repo.get_by_id(db, role_id)
    res = role_repo.delete(db, role_model)
    if not res:
        raise HTTPException(404, "Role not found")

