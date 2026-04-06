from sqlmodel import Session
import backend.repositories.registration as registration_repo
import backend.schemas.registration as registration_schema
from backend.models.registration import Registration as RegistrationModel


def get_all(db: Session):
    return registration_repo.get_all(db)


def get(
    db: Session,
    registration_id: int,
):
    return registration_repo.get_by_id(db, registration_id)


def create(db: Session, registration_data: registration_schema.RegistrationCreate):
    registration_model = RegistrationModel(
        user_id=registration_data.user_id, event_id=registration_data
    )
    return registration_repo.create(db, registration_model)


def delete(
    db: Session,
    registration_id: int,
):
    registration_model = registration_repo.get_by_id(db, registration_id)
    return registration_repo.delete(db, registration_model)

