from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from app.core.security import ALLOW_ADMIN, ALLOW_USER
from app.db.session import get_session
from app.schemas.registration import (
    RegistrationCreate,
    RegistrationUpdate,
    RegistrationResponse,
)
from app.services.registration import RegistrationService

router = APIRouter()


def get_registration_service(session: Session = Depends(get_session)):
    return RegistrationService(session)


@router.get(
    "/", response_model=list[RegistrationResponse], status_code=status.HTTP_200_OK
)
def get_registrations(
    auth=Depends(ALLOW_ADMIN),
    service: RegistrationService = Depends(get_registration_service),
):
    return service.get_all()


@router.get(
    "/{registration_id}",
    response_model=RegistrationResponse,
    status_code=status.HTTP_200_OK,
)
def get_registration(
    registration_id: int,
    auth=Depends(ALLOW_USER),
    service: RegistrationService = Depends(get_registration_service),
):
    registration = service.get_by_id(registration_id)
    if not registration:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Registration not found",
        )
    return registration


@router.post(
    "/", response_model=RegistrationResponse, status_code=status.HTTP_201_CREATED
)
def create_registration(
    data: RegistrationCreate,
    auth=Depends(ALLOW_USER),
    service: RegistrationService = Depends(get_registration_service),
):
    return service.create(data)


@router.put(
    "/{registration_id}",
    response_model=RegistrationResponse,
    status_code=status.HTTP_200_OK,
)
def update_registration(
    registration_id: int,
    data: RegistrationUpdate,
    auth=Depends(ALLOW_ADMIN),
    service: RegistrationService = Depends(get_registration_service),
):
    registration = service.update(registration_id, data)
    if not registration:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Registration not found",
        )
    return registration


@router.delete("/{registration_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_registration(
    registration_id: int,
    auth=Depends(ALLOW_ADMIN),
    service: RegistrationService = Depends(get_registration_service),
):
    deleted = service.delete(registration_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Registration not found",
        )
    return None