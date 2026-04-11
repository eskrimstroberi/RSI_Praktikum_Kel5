from sqlmodel import SQLModel, Field


class Item(SQLModel, table=True):
    __tablename__ = "Item"

    id: int = Field(primary_key=True, index=True)
    name: str = Field(max_length=100, nullable=False)
    price: float = Field(default=0.0)
    description: str | None = Field(max_length=255, nullable=True)
