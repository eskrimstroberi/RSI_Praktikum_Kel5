from fastapi import HTTPException
from sqlmodel import Session
from app.models.account import Account as AccountModel
import app.schemas.account as account_schema
from app.repositories.account import AccountRepository
from app.repositories.user import UserRepository
from app.repositories.role import RoleRepository


class AccountService:
    def __init__(self, session: Session):
        self.repo = AccountRepository(session)
        self.user_repo = UserRepository(session)
        self.role_repo = RoleRepository(session)

    def create(self, data: account_schema.AccountCreate):
        user = self.user_repo.get_by_id(data.user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        role = self.role_repo.get_by_id(data.role_id)
        if not role:
            raise HTTPException(status_code=404, detail="Role not found")

        account = AccountModel(**data.model_dump())
        return self.repo.create(account)

    def get_all(self):
        return self.repo.get_all()

    def get_by_id(self, id: int):
        db_item = self.repo.get_by_id(id)
        if not db_item:
            raise HTTPException(status_code=404, detail="Account not found")
        return db_item

    def delete(self, id: int):
        db_item = self.repo.get_by_id(id)
        if not db_item:
            raise HTTPException(status_code=404, detail="Account not found")

        return self.repo.delete(db_item)
