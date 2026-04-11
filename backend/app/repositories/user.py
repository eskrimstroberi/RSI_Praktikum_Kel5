from sqlmodel import Session
from app.models.user import User as UserModel
from app.repositories.base import BaseRepository


class UserRepository(BaseRepository[UserModel]):
    def __init__(self, session: Session):
        super().__init__(model=UserModel, session=session)
