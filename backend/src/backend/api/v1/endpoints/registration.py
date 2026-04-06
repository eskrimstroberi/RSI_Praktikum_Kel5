from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from backend.db.session import get_db
from backend.schemas.registration import (
    RegistrationCreate,
    RegistrationUpdate,
    RegistrationResponse,
)
from backend.services.registration import RegistrationService

router = APIRouter()

service = RegistrationService()


@router.get("/", response_model=list[RegistrationResponse], status_code=status.HTTP_200_OK)
def get_registrations(db: Session = Depends(get_db)):
    return service.get_registrations(db)


@router.get(
    "/{registration_id}",
    response_model=RegistrationResponse,
    status_code=status.HTTP_200_OK
)
def get_registration(registration_id: int, db: Session = Depends(get_db)):
    registration = service.get_registration(db, registration_id)
    if not registration:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Registration not found"
        )
    return registration


@router.post("/", response_model=RegistrationResponse, status_code=status.HTTP_201_CREATED)
def create_registration(data: RegistrationCreate, db: Session = Depends(get_db)):
    return service.create_registration(db, data)


@router.put(
    "/{registration_id}",
    response_model=RegistrationResponse,
    status_code=status.HTTP_200_OK
)
def update_registration(
    registration_id: int,
    data: RegistrationUpdate,
    db: Session = Depends(get_db)
):
    registration = service.update_registration(db, registration_id, data)
    if not registration:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Registration not found"
        )
    return registration


@router.delete("/{registration_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_registration(registration_id: int, db: Session = Depends(get_db)):
    deleted = service.delete_registration(db, registration_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Registration not found"
        )
    return None