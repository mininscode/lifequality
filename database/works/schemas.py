from pydantic import BaseModel


class Work(BaseModel):
    id: int
    name: str
    is_emergency: bool
    duration: int

    class Config:
        orm_mode = True

