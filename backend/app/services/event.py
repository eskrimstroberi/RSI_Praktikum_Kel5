from fastapi import HTTPException
from sqlmodel import Session

from app.models.event import Event as EventModel
from app.schemas.event import EventCreate, EventUpdate
from app.repositories.event import EventRepository


class EventService:
    def __init__(self, session: Session):
        self.repo = EventRepository(session)

    def get_all(self):
        return self.repo.get_all()

    def get_by_id(self, id: int):
        return self.repo.get_by_id(id)

    def create(self, data: EventCreate):
        model_item = EventModel(**data.model_dump())
        return self.repo.create(model_item)

    def update(self, id: int, data: EventUpdate):
        db_item = self.repo.get_by_id(id)
        if not db_item:
            raise HTTPException(404, "Item cannot be found.")
        return self.repo.update(id, db_item.model_dump(exclude_unset=True))

    def delete(self, id: int):
        db_item = self.repo.get_by_id(id)
        if not db_item:
            raise HTTPException(404, "Item cannot be found.")
        return self.repo.delete(db_item)
