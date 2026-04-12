from fastapi import HTTPException, Response
from sqlmodel import Session

from app.core.security import create_access_token, hash_password, verify_password
import app.schemas.account as account_schema
from app.models.account import Account as AccountModel
from app.repositories.account import AccountRepository
from app.repositories.role import RoleRepository
from app.repositories.user import UserRepository


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
        account.password = hash_password(data.password)
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

    def login(self, data: account_schema.AccountLogin, response: Response):
        account = self.repo.get_by_username(data.username)
        if not account:
            raise HTTPException(status_code=404, detail="Account not found.")

        password_correct = verify_password(account.password, data.password)
        if not password_correct:
            raise HTTPException(
                status_code=401, detail="Incorrect username or password."
            )

        token_data = {"sub": str(account.id)}
        access_token = create_access_token(data=token_data)
        response.set_cookie(
            key="access_token",
            value=f"Bearer {access_token}",
            httponly=True,
            max_age=(86400 * 7),
            samesite="lax",
            secure=True,
        )

        return True

    def logout(self, response: Response):
        response.delete_cookie(
            key="access_token",
            httponly=True,
            samesite="lax",
            secure=True,
        )
        return True
