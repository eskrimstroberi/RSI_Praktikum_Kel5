from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from backend.db.session import get_db
from backend.schemas.event import EventCreate, EventUpdate, EventResponse
from backend.services.event import EventService

router = APIRouter()

service = EventService()


@router.get("/", response_model=list[EventResponse], status_code=status.HTTP_200_OK)
def get_events(db: Session = Depends(get_db)):
    return service.get_events(db)


@router.get("/{event_id}", response_model=EventResponse, status_code=status.HTTP_200_OK)
def get_event(event_id: int, db: Session = Depends(get_db)):
    event = service.get_event(db, event_id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event not found"
        )
    return event


@router.post("/", response_model=EventResponse, status_code=status.HTTP_201_CREATED)
def create_event(data: EventCreate, db: Session = Depends(get_db)):
    return service.create_event(db, data)


@router.put("/{event_id}", response_model=EventResponse, status_code=status.HTTP_200_OK)
def update_event(
    event_id: int,
    data: EventUpdate,
    db: Session = Depends(get_db)
):
    event = service.update_event(db, event_id, data)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event not found"
        )
    return event


@router.delete("/{event_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_event(event_id: int, db: Session = Depends(get_db)):
    deleted = service.delete_event(db, event_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Event not found"
        )
    return None