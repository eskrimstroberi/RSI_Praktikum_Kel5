from fastapi import HTTPException
from sqlmodel import Session, select
from sqlalchemy.orm import selectinload
from app.models.account import Account as AccountModel
from app.repositories.base import BaseRepository


class AccountRepository(BaseRepository[AccountModel]):
    def __init__(self, session: Session):
        super().__init__(model=AccountModel, session=session)

    def get_by_username(self, data: str):
        query = select(self.model).where(self.model.username == data)
        return self.session.exec(query).one_or_none()

    def get_with_roles_by_id(self, id: int):
        query = (
            select(AccountModel)
            .where(AccountModel.id == id)
            .options(selectinload(AccountModel.role), selectinload(AccountModel.user))
        )
        return self.session.exec(query).one_or_none()
