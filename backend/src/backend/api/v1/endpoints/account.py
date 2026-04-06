from fastapi import Depends, APIRouter
from sqlmodel import Session

from backend.db.session import get_db
from backend.schemas.account import AccountCreate
from backend.services.account import (
    create_account_service,
    get_all_accounts_service,
    get_account_by_id_service,
    delete_account_service,
)

router = APIRouter()


@router.get("/")
def get_accounts(db: Session = Depends(get_db)):
    return get_all_accounts_service(db)


@router.get("/{account_id}")
def get_account(account_id: int, db: Session = Depends(get_db)):
    return get_account_by_id_service(db, account_id)


@router.post("/")
def create_account(data: AccountCreate, db: Session = Depends(get_db)):
    return create_account_service(db, data)


@router.delete("/{account_id}")
def delete_account(account_id: int, db: Session = Depends(get_db)):
    return delete_account_service(db, account_id)

