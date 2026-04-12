from fastapi import Depends, APIRouter, Request, Response
from sqlmodel import Session

from app.core.security import get_current_user
from app.db.session import get_session
from app.schemas.account import AccountCreate, AccountResponse, AccountLogin
from app.services.account import AccountService

router = APIRouter()


def get_account_service(session: Session = Depends(get_session)):
    return AccountService(session)


@router.get("/", response_model=list[AccountResponse])
def get_accounts(service: AccountService = Depends(get_account_service)):
    return service.get_all()


@router.get("/{account_id}", response_model=AccountResponse)
def get_account(
    account_id: int, service: AccountService = Depends(get_account_service)
):
    return service.get_by_id(account_id)


@router.post("/", response_model=AccountResponse)
def create_account(
    data: AccountCreate, service: AccountService = Depends(get_account_service)
):
    return service.create(data)


@router.delete("/{account_id}")
def delete_account(
    account_id: int, service: AccountService = Depends(get_account_service)
):
    return service.delete(account_id)


@router.post("/login")
def login(
    data: AccountLogin,
    response: Response,
    service: AccountService = Depends(get_account_service),
):
    if service.login(data, response):
        return {"message": "Successfully logged in"}


@router.post("/logout")
def logout(
    response: Response,
    service: AccountService = Depends(get_account_service),
):
    if service.logout(response):
        return {"message": "Successfully logged out"}
