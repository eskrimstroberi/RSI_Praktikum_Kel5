from sqlmodel import Session

from app.models.registration import Registration as RegistrationModel
from app.schemas.registration import RegistrationCreate, RegistrationUpdate


class RegistrationService:
    def get_registrations(self, db: Session):
        return db.query(RegistrationModel).all()

    def get_registration(self, db: Session, registration_id: int):
        return db.get(RegistrationModel, registration_id)

    def create_registration(self, db: Session, data: RegistrationCreate):
        registration = RegistrationModel(**data.model_dump())
        db.add(registration)
        db.commit()
        db.refresh(registration)
        return registration

    def update_registration(
        self, db: Session, registration_id: int, data: RegistrationUpdate
    ):
        registration = db.get(RegistrationModel, registration_id)
        if not registration:
            return None

        for key, value in data.model_dump().items():
            setattr(registration, key, value)

        db.commit()
        return registration

    def delete_registration(self, db: Session, registration_id: int):
        registration = db.get(RegistrationModel, registration_id)
        if not registration:
            return False

        db.delete(registration)
        db.commit()
        return True

