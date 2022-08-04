from pydantic import BaseModel


class Employee(BaseModel):
    id: int
    name: str
    surname: str
    patronymic: str
    department: str
    position: str
    employee_number: int
    user_id: int

    class Config:
        orm_mode = True

