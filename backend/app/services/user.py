from sqlmodel import Session

from app.models.user import User as UserModel
from app.schemas.user import UserCreate, UserUpdate


class UserService:
    def get_users(self, db: Session):
        return db.query(UserModel).all()

    def get_user(self, db: Session, user_id: int):
        return db.get(UserModel, user_id)

    def create_user(self, db: Session, data: UserCreate):
        user = UserModel(**data.model_dump())
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    def update_user(self, db: Session, user_id: int, data: UserUpdate):
        user = db.get(UserModel, user_id)
        if not user:
            return None

        for key, value in data.model_dump().items():
            setattr(user, key, value)

        db.commit()
        return user

    def delete_user(self, db: Session, user_id: int):
        user = db.get(UserModel, user_id)
        if not user:
            return False

        db.delete(user)
        db.commit()
        return True