from pydantic import BaseModel


class RequestStatus(BaseModel):
    id: int
    name: str

