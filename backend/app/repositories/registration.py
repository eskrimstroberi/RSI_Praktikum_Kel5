from sqlmodel import Session, select
from app.models.registration import Registration as RegistrationModel


def create(db: Session, registration: RegistrationModel):
    db.add(registration)
    db.commit()
    db.refresh(registration)
    return registration


def get_all(db: Session):
    query = select(RegistrationModel)
    res = db.exec(query).all()
    return res


def get_by_id(db: Session, registration_id: int):
    res = db.get_one(RegistrationModel, registration_id)
    return res


def delete(db: Session, registration: RegistrationModel):
    db.delete(registration)
    db.commit()
