from sqlmodel import Session, select
from backend.models.account import Account as AccountModel


def create(db: Session, account: AccountModel):
    db.add(account)
    db.commit()
    db.refresh(account)
    return account


def get_by_id(db: Session, account_id: int):
    res = db.get_one(AccountModel, account_id)
    return res


def get_all(db: Session):
    query = select(AccountModel)
    res = db.exec(query).all()
    db.commit()
    return res


def delete(db: Session, account: AccountModel):
    db.delete(account)
    db.commit()
