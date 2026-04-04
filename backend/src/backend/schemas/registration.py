from pydantic import BaseModel, ConfigDict

class RegistrationBase(BaseModel):
    user_id: int
    event_id: int

class RegistrationCreate(RegistrationBase):
    pass

class RegistrationResponse(RegistrationBase):
    id: int

    model_config = ConfigDict(from_attributes=True)