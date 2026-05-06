from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from app.core.security import ALLOW_ADMIN, ALLOW_USER
from app.db.session import get_session
from app.schemas.event import EventCreate, EventUpdate, EventResponse
from app.services.event import EventService

router = APIRouter()


def get_event_service(session: Session = Depends(get_session)):
    return EventService(session)


@router.get("/", response_model=list[EventResponse], status_code=status.HTTP_200_OK)
def get_events(
    auth=Depends(ALLOW_USER), service: EventService = Depends(get_event_service)
):
    return service.get_all()


@router.get("/{event_id}", response_model=EventResponse, status_code=status.HTTP_200_OK)
def get_event(
    event_id: int,
    auth=Depends(ALLOW_USER),
    service: EventService = Depends(get_event_service),
):
    event = service.get_by_id(event_id)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Event not found"
        )
    return event


@router.post("/", response_model=EventResponse, status_code=status.HTTP_201_CREATED)
def create_event(
    data: EventCreate,
    auth=Depends(ALLOW_ADMIN),
    service: EventService = Depends(get_event_service),
):
    return service.create(data)


@router.put("/{event_id}", response_model=EventResponse, status_code=status.HTTP_200_OK)
def update_event(
    event_id: int,
    data: EventUpdate,
    auth=Depends(ALLOW_ADMIN),
    service: EventService = Depends(get_event_service),
):
    event = service.update(event_id, data)
    if not event:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Event not found"
        )
    return event


@router.delete("/{event_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_event(
    event_id: int,
    auth=Depends(ALLOW_ADMIN),
    service: EventService = Depends(get_event_service),
):
    deleted = service.delete(event_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Event not found"
        )
    return None
