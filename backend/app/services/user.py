from fastapi import HTTPException
from sqlmodel import Session

from app.models.user import User as UserModel
from app.schemas.user import UserCreate, UserUpdate
from app.repositories.user import UserRepository


class UserService:
    def __init__(self, session: Session):
        self.repo = UserRepository(session)

    def get_all(self):
        return self.repo.get_all()

    def get_by_id(self, id: int):
        return self.repo.get_by_id(id)

    def create(self, data: UserCreate):
        model_item = UserModel(**data.model_dump())
        db_item = self.repo.create(model_item)
        return db_item

    def update_user(self, id: int, data: UserUpdate):
        return self.repo.update(id, data.model_dump(exclude_unset=True))

    def delete(self, id: int):
        db_item = self.repo.get_by_id(id)
        if not db_item:
            raise HTTPException(404, "Item cannot be found.")
        return self.repo.delete(db_item)
