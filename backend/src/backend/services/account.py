from datetime import datetime
from fastapi import HTTPException
from sqlmodel import Session
import backend.schemas.account as account_schema
import backend.repositories.account as account_repo
from backend.models.user import User as UserModel
from backend.models.account import Account as AccountModel
from backend.models.role import Role as RoleModel


def create_account_service(db: Session, account_data: account_schema.AccountCreate):
    user = db.get(UserModel, account_data.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    role = db.get(RoleModel, account_data.role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")

    now = datetime.now()
    account = AccountModel(
        **account_data.model_dump(),
        created_at=now,
        updated_at=now,
    )
    res = account_repo.create(db, account)
    return res


def get_all_accounts_service(db: Session):
    return account_repo.get_all(db)


def get_account_by_id_service(db: Session, account_id: int):
    account = account_repo.get_by_id(db, account_id)
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    return account


def delete_account_service(db: Session, account_id: int):
    account = account_repo.get_by_id(db, account_id)
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    account_repo.delete(db, account)
    return {"message": "Account deleted successfully"}