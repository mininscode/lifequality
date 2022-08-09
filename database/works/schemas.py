from datetime import datetime
from pydantic import BaseModel


class Work(BaseModel):
    id: int
    name: str
    is_emergency: bool
    duration: datetime

    class Config:
        orm_mode = True

