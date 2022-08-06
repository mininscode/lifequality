from datetime import date
from pydantic import BaseModel


class Contract(BaseModel):
    id: int
    contract_number: int
    contract_date: date
    contract_file: str
    house_id: int
    contractor_id: int

    class Config:
        orm_mode = True

