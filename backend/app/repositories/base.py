from typing import Any, TypeVar, Generic
from sqlmodel import Session, select
from pydantic import BaseModel
from app.db.base import SQLModel

T = TypeVar("T", bound=SQLModel)


class BaseRepository(Generic[T]):
    def __init__(self, model: type[T], session: Session):
        self.model = model
        self.session = session

    def create(self, obj_in: T) -> T:
        self.session.add(obj_in)
        self.session.commit()
        self.session.refresh(obj_in)
        return obj_in

    def get_all(self):
        query = select(self.model)
        res = self.session.exec(query).all()
        return res

    def get_by_id(self, id: int):
        return self.session.get(self.model, id)

    def update(self, id: int, data: dict[str, Any] | BaseModel | T) -> T | None:
        db_obj = self.get_by_id(id)
        if not db_obj:
            return None

        if isinstance(data, dict):
            update_data = data
        elif isinstance(data, BaseModel):
            update_data = data.model_dump(exclude_unset=True)
        else:
            update_data = {
                k: v for k, v in data.__dict__.items() if k != "_sa_instance_state"
            }

        for field, value in update_data.items():
            if hasattr(db_obj, field):
                setattr(db_obj, field, value)

        self.session.commit()
        self.session.refresh(db_obj)
        return db_obj

    def delete(self, obj_in: T):
        self.session.delete(obj_in)
        self.session.commit()
        return True
