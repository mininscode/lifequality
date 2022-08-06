from pydantic import BaseModel


class Contractor(BaseModel):
    id: int
    name: str
    contract: int
    house: int

    class Config:
        orm_mode = True

