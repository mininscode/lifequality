from pydantic import BaseModel

from database.clients.schemas import Client
from database.meetings.schemas import Meeting
from database.contracts.schemas import Contract
from database.contractors.schemas import Contractor


class House(BaseModel):
    id: int
    city: str
    district: str
    street: str
    house_number: str
    condition: str

    citizens: list[Client] = []
    meetings: list[Meeting] = []
    contracts: list[Contract] = []
    contractors: list[Contractor] = []

    class Config:
        orm_mode = True

