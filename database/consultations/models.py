from sqlalchemy.orm import relationship
from sqlalchemy import Column, BigInteger, DateTime, String

from database import  Base
from database.models_associations import association_client_request_with_consultation_table, \
        association_consultation_with_employee_table


class Consultation(Base):
    __tablename__ = 'consultations'

    id = Column(BigInteger, primary_key=True, index=True)
    created_at = Column(DateTime, nullable=False)
    text = Column(String(200), nullable=False)

    citizen = relationship('Client', back_populates='consultations')
    
    citizen_requests = relationship('ClientRequest', \
            secondary=association_client_request_with_consultation_table, \
            back_populates='consultations')

    employees = relationship('Employee', \
            secondary=association_consultation_with_employee_table, \
            back_populates='consultations')

