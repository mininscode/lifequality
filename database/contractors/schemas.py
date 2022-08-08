from pydantic import BaseModel


class Contractor(BaseModel):
    id: int
    name: str
    city: str
    street: str
    building: int
    contract_id: int
    user_id: int

    class Config:
        orm_mode = True

