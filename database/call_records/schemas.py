from datetime import datetime
from pydantic import BaseModel


class CallRecord(BaseModel):
    id: int
    file_path: str
    created_at: datetime
    citizen_id: int
    employee_id: int

    class Config:
        orm_mode = True

