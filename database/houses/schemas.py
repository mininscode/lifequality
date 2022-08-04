from pydantic import BaseModel

from database.clients.schemas import Client
# from database.treatments.schemas import Treatment
# from database.meetings.schemas import Meeting
# from database.contractors.schemas import Contractor


class House(BaseModel):
    id: int
    city: str
    district: str
    street: str
    house_number: str
    condition: str

    citizens: list[Client] = []
    # treatments: list[Treatment] = []
    # meetings: list[Meeting] = []
    # contractors: list[Contractor] = []

    class Config:
        orm_mode = True

