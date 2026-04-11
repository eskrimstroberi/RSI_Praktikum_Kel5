from sqlmodel import Field, SQLModel, Relationship


class Registration(SQLModel, table=True):
    __tablename__: str = "Registration"

    id: int = Field(primary_key=True, index=True)

    user_id: int = Field(foreign_key="User.id", nullable=False)

    event_id: int = Field(foreign_key="Event.id", nullable=False)

    user: "User" = Relationship(back_populates="registrations")
    event: "Event" = Relationship(back_populates="registrations")
