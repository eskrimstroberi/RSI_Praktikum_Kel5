from pydantic import BaseModel
from typing import Optional
from .user import UserResponse
from .event import EventResponse


class RegistrationBase(BaseModel):
    user_id: int
    event_id: int


class RegistrationCreate(RegistrationBase):
    pass


class RegistrationUpdate(RegistrationBase):
    pass


class RegistrationResponse(RegistrationBase):
    id: int

    class Config:
        from_attributes = True


class RegistrationDetail(RegistrationResponse):
    user: Optional[UserResponse] = None
    event: Optional[EventResponse] = None