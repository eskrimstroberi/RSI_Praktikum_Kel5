from sqlmodel import SQLModel
from sqlmodel.main import SQLModelConfig


class ItemBase(SQLModel):
    id: int | None = None
    name: str

    model_config: SQLModelConfig = SQLModelConfig(from_attributes=True)


class ItemCreate(SQLModel):
    name: str


class ItemUpdate(ItemBase):
    name: str
