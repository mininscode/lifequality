from sqlalchemy.orm import relationship
from sqlalchemy import Column, BigInteger, Integer, String, ForeignKey

from database import Base
from database.models_associations import association_client_request_with_employee_table, \
        association_consultation_with_employee_table


class Employee(Base):
    __tablename__ = 'employees'

    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    patronymic = Column(String(50), nullable=False)
    department = Column(String(150), nullable=False)
    position = Column(String(80), nullable=False)
    employee_number = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    user = relationship('User', back_populates='employees')
    records = relationship('CallRecord', back_populates='records')

    citizen_requests = relationship('ClientRequest', \
            secondary=association_client_request_with_employee_table, \
            back_populates='employees')

    consultations = relationship('Consultation', \
            secondary=association_consultation_with_employee_table, \
            back_populates='employees')

