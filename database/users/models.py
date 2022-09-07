from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from database import Base
from database.contractors.models import Contractor
from database.employees.models import Employee
from database.clients.models import Client


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    is_active = Column(Boolean, default=True)

    citizens = relationship('Client', back_populates='user')
    contractors = relationship('Contractor', back_populates='user')
    employees = relationship('Employee', back_populates='user')

