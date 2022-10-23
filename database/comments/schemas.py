from datetime import datetime
from pydantic import BaseModel


class Comment(BaseModel):
    id: int
    text: str
    author_id: int
    created_at: datetime
    citizen_request_id: int
    
    class Config:
        orm_mode = True

