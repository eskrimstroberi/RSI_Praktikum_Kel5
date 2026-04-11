from sqlmodel import Session
from app.models.account import Account as AccountModel
from app.repositories.base import BaseRepository


class AccountRepository(BaseRepository[AccountModel]):
    def __init__(self, session: Session):
        super().__init__(model=AccountModel, session=session)
