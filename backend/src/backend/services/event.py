from sqlmodel import Session

from backend.models.event import Event as EventModel
from backend.schemas.event import EventCreate, EventUpdate


class EventService:
    def get_events(self, db: Session):
        return db.query(EventModel).all()

    def get_event(self, db: Session, event_id: int):
        return db.get(EventModel, event_id)

    def create_event(self, db: Session, data: EventCreate):
        event = EventModel(**data.model_dump())
        db.add(event)
        db.commit()
        db.refresh(event)
        return event

    def update_event(self, db: Session, event_id: int, data: EventUpdate):
        event = db.get(EventModel, event_id)
        if not event:
            return None

        for key, value in data.model_dump().items():
            setattr(event, key, value)

        db.commit()
        db.refresh(event)
        return event

    def delete_event(self, db: Session, event_id: int):
        event = db.get(EventModel, event_id)
        if not event:
            return False

        db.delete(event)
        db.commit()
        return True