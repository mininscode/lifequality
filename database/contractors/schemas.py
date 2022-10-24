from pydantic import BaseModel


class Contractor(BaseModel):
    id: int
    name: str
    city: str
    street: str
    building: int
    user_id: int
    is_emergency_service: bool

    class Config:
        orm_mode = True

