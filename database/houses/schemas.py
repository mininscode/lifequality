from pydantic import BaseModel

from database.citizens.schemas import Citizen


class House(BaseModel):
    id: int
    city: str
    street: str
    house_number: str
    citizens: list[Citizen] = []

    class Config:
        orm_mode = True

