from datetime import datetime
from pydantic import BaseModel


class CallRecord(BaseModel):
    file_path: str
    created_at: datetime
    citizen_id: int
    employee_id: int

class CitizenRequestCallRecord(CallRecord):
    id: int
    citizen_request_id: int

    class Config:
        orm_mode = True

class ConsultationCallRecord(CallRecord):
    id: int
    consultation_id: int

    class Config:
        orm_mode = True

