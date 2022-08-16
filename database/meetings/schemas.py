from datetime import date
from pydantic import BaseModel


class Meeting(BaseModel):
    id: int
    meeting_date: date
    house_id: int
    is_legal: bool
    meeting_record: str

    class Config:
        orm_method = True

