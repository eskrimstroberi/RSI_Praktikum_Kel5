from fastapi import HTTPException
from sqlmodel import Session

from app.models.registration import Registration as RegistrationModel
from app.schemas.registration import RegistrationCreate, RegistrationUpdate
from app.repositories.registration import RegistrationRepository


class RegistrationService:
    def __init__(self, session: Session):
        self.repo = RegistrationRepository(session)

    def get_all(self):
        return self.repo.get_all()

    def get_by_id(self, id: int):
        return self.repo.get_by_id(id)

    def create(self, data: RegistrationCreate):
        model_item = RegistrationModel(**data.model_dump())
        return self.repo.create(model_item)

    def update(self, id: int, data: RegistrationUpdate):
        registration = self.repo.get_by_id(id)
        if not registration:
            raise HTTPException(status_code=404, detail="Registration not found")
        return self.repo.update(id, data.model_dump(exclude_unset=True))

    def delete(self, id: int):
        db_item = self.repo.get_by_id(id)
        if not db_item:
            raise HTTPException(status_code=404, detail="User not found")

        return self.repo.delete(db_item)
