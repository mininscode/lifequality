from pydantic import BaseModel


class RequestStatus(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

