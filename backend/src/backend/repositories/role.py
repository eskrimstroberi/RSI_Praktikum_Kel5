from sqlmodel import Session, select
from backend.models.role import Role as RoleModel


def create(db: Session, role: RoleModel):
    db.add(role)
    db.commit()
    db.refresh(role)
    return role


def get_all(db: Session):
    query = select(RoleModel)
    res = db.exec(query).all()
    return res


def get_by_id(db: Session, role_id: int):
    res = db.get_one(RoleModel, role_id)
    return res


def delete(db: Session, role: RoleModel):
    db.delete(role)
    db.commit()
