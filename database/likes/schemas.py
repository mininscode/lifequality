from datetime import datetime
from pydantic import BaseModel


class Like(BaseModel):
    id: int
    citizen_request_id: int
    count: int
    author_id: int
    created_at: datetime

    class Config:
        orm_mode = True

