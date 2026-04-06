from sqlmodel import Session, select

from backend.models.role import Role as RoleModel
from backend.schemas.role import RoleCreate


class RoleService:
    def get_roles(self, db: Session):
        return db.exec(select(RoleModel)).all()

    def get_role(self, db: Session, role_id: int):
        return db.get(RoleModel, role_id)

    def create_role(self, db: Session, data: RoleCreate):
        role = RoleModel(**data.model_dump())
        db.add(role)
        db.commit()
        db.refresh(role)
        return role

    def delete_role(self, db: Session, role_id: int):
        role = db.get(RoleModel, role_id)
        if not role:
            return False

        db.delete(role)
        db.commit()
        return True

