from pydantic import BaseModel


class RequestSource(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True

