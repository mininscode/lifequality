from datetime import datetime
from pydantic import BaseModel


class Consultation(BaseModel):
    id: int
    created_at: datetime
    text: str
    employee_id: int
    record_id: int

    class Config:
        orm_mode = True

