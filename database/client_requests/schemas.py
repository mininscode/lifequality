from datetime import datetime
from pydantic import BaseModel

from validation_types import AddressType


class ClientRequest(BaseModel):
    id: int
    text: str
    citizen_id: int
    address: AddressType
    request_source: int
    created_at: datetime
    updated_at: datetime
    closed_at: datetime
    fact_duration: datetime
    request_status: int
    citizen_feedback: str
    is_active: bool
    record_id: int
    
    class Config:
        orm_mode = True
    
