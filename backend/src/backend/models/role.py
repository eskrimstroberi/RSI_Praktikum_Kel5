from sqlmodel import SQLModel, Field, Relationship


class Role(SQLModel, table=True):
    __tablename__ = "Role"

    id: int = Field(primary_key=True, index=True)
    name: str = Field(max_length=255)

    accounts: list["Account"] = Relationship(back_populates="role")
