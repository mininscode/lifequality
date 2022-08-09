from datetime import datetime
from pydantic import BaseModel


class WorkOrder(BaseModel):
    id: int
    file_path: str
    created_at: datetime
    citizen_request_id: int
    contractor_id: int
    
    class Config:
        orm_mode = True

