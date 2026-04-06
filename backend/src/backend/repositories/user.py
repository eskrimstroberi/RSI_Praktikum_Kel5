from sqlmodel import Session, select
from backend.schemas.user import UserBase
from backend.models.user import User as UserModel


def create(db: Session, user: UserBase):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


# GET ALL
def get_all(db: Session):
    query = select(UserBase)
    res = db.exec(query).all()
    return res


def get_by_id(db: Session, user_id: int):
    return db.get(UserBase, user_id)


def update(db: Session, user_id: int, user_data: UserModel):
    user = db.get_one(UserModel, user_id)

    if not user:
        return None

    if user_data.first_name is not None:
        user.first_name = user_data.first_name
    if user_data.last_name is not None:
        user.last_name = user_data.last_name
    if user_data.whatsapp is not None:
        user.whatsapp = user_data.whatsapp

    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def delete(db: Session, user: UserModel):
    db.delete(user)
    db.commit()
