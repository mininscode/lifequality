from datetime import date
from pydantic import BaseModel


class Contract(BaseModel):
    id: int
    contract_number: int
    contract_date: date
    expiration_date: date
    contractor_id: int
    house_id: int
    is_active: bool

    class Config:
        orm_mode = True

