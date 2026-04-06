from sqlmodel import Session
import backend.repositories.event as event_repo
import backend.schemas.event as event_schema
from backend.models.event import Event as EventModel


def get_all(db: Session):
    return event_repo.get_all(db)


def get(db: Session, event_id: int):
    return event_repo.get_by_id(db, event_id)


def create(db: Session, event_data: event_schema.EventCreate):
    event_model = EventModel(name=event_data.name, description=event_data.description)
    return event_repo.create(db, event_model)


def update(db: Session, event_id: int, event_data: event_schema.EventUpdate):
    event_model = EventModel(
        id=event_id, name=event_data.name, description=event_data.description
    )
    return event_repo.update(db, event_model)


def delete(db: Session, event_id: int):
    event = event_repo.get_by_id(db, event_id)
    return event_repo.delete(db, event)

