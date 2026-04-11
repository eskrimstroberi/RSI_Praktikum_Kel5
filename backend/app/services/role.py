from fastapi import HTTPException
from sqlmodel import Session

from app.models.role import Role as RoleModel
from app.repositories.role import RoleRepository
from app.schemas.role import RoleCreate


class RoleService:
    def __init__(self, session: Session):
        self.repo = RoleRepository(session)

    def get_all(self):
        return self.repo.get_all()

    def get_by_id(self, id: int):
        return self.repo.get_by_id(id)

    def create(self, data: RoleCreate):
        model_item = RoleModel(**data.model_dump())
        db_item = self.repo.create(model_item)
        return db_item

    def delete(self, id: int):
        db_item = self.repo.get_by_id(id)
        if not db_item:
            raise HTTPException(404, "Item cannot be found.")
        return self.repo.delete(db_item)
