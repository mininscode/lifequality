from datetime import datetime
from pydantic import BaseModel


class Comment(BaseModel):
    id: int
    text: str
    author: str
    created_at: datetime
    citizen_request_id: int
    
    class Config:
        orm_mode = True

