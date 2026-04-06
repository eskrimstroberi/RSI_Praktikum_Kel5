from sqlmodel import Session, select
from backend.models.event import Event as EventModel


def get_all(db: Session):
    query = select(EventModel)
    res = db.exec(query).all()
    return res


def get_by_id(db: Session, event_id: int):
    res = db.get_one(EventModel, event_id)
    return res


def create(db: Session, event: EventModel):
    db.add(event)
    db.commit()
    db.refresh(event)
    return event


def update(db: Session, event: EventModel):
    db.add(event)
    db.commit()
    db.refresh(event)
    return event


def delete(db: Session, event: EventModel):
    db.delete(event)
    db.commit()
