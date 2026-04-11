from sqlmodel import Session
from app.models.event import Event as EventModel
from app.repositories.base import BaseRepository


class EventRepository(BaseRepository[EventModel]):
    def __init__(self, session: Session):
        super().__init__(model=EventModel, session=session)
