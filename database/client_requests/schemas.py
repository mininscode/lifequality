from datetime import datetime
from pydantic import BaseModel

from validation_types import AddressType


class ClientRequest(BaseModel):
    id: int
    text: str
    citizen_id: int
    address: AddressType
    request_source: str
    created_at: datetime
    updated_at: datetime
    closed_at: datetime
    planed_duration: datetime
    fact_duration: datetime
    request_status: str
    citizen_feedback: str
    is_active: bool
    
    class Config:
        orm_mode = True
    
