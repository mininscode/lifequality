from datetime import date
from pydantic import BaseModel


class ClientBase(BaseModel):
    name: str
    surname: str
    patronymic: str

class ClientPassport(BaseModel):
    id: int
    passport_serial: str
    passport_number: int
    passport_date: date
    passport_office: str
    citizen_id: int
    is_active: bool

    class Config:
        orm_mode = True

class Client(ClientBase):
    id: int
    house_id: int
    flat_number: int
    is_registered: bool
    user_id: int

    class Config:
        orm_mode = True

