from sqlmodel import Session
from app.models.registration import Registration as RegistrationModel
from app.repositories.base import BaseRepository


class RegistrationRepository(BaseRepository[RegistrationModel]):
    def __init__(self, session: Session):
        super().__init__(model=RegistrationModel, session=session)
