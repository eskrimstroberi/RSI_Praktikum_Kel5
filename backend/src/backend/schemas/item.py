from pydantic import BaseModel


class ItemBase(BaseModel):
    id: int | None = None
    name: str


class ItemCreate(BaseModel):
    name: str


class ItemUpdate(ItemBase):
    name: str
