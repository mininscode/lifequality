from datetime import datetime
from pydantic import BaseModel
from typing import Literal


class RequestDocument(BaseModel):
    id: int
    document_type: Literal['work_order'] | Literal['act_of_done_works']
    file_path: str
    created_at: datetime
    citizen_request_id: int
    contractor_id: int
    
    class Config:
        orm_mode = True

