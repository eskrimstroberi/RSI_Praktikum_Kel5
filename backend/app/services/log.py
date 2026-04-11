from sqlmodel import Session
from fastapi import HTTPException

from app.models.log import Log as LogModel
from app.schemas.log import LogCreate, LogUpdate, LogPatch
from app.repositories.log import LogRepository


class LogService:
    def __init__(self, session: Session):
        self.repo = LogRepository(session)

    def get_all(self):
        return self.repo.get_all()

    def get_by_id(self, id: int):
        return self.repo.get_by_id(id)

    def create(self, data: LogCreate):
        model_item = LogModel(**data.model_dump())
        db_item = self.repo.create(model_item)
        return db_item

    def put(self, id: int, data: LogUpdate):
        return self.repo.update(id, data.model_dump())

    def patch(self, id: int, data: LogPatch):
        return self.repo.update(id, data.model_dump(exclude_unset=True))

    def delete(self, id: int):
        db_item = self.repo.get_by_id(id)
        if not db_item:
            raise HTTPException(404, "Item cannot be found.")

        db_item = self.repo.delete(db_item)
        return db_item
