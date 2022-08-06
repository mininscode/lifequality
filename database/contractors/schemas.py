from pydantic import BaseModel


class Contractor(BaseModel):
    id: int
    name: str
    contract_id: int
    house_id: int

    class Config:
        orm_mode = True

