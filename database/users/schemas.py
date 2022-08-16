from pydantic import BaseModel, EmailStr

from database.clients.models import Client


class UserBase(BaseModel):
    email: EmailStr
    phone: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    clients: list[Client]

    class Config:
        orm_mode = True
