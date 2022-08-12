from sqlalchemy.orm import relationship
from sqlalchemy import Column, BigInteger, ForeignKey, DateTime, String, \
                       Integer

from database import  Base


class Consultation(Base):
    __tablename__ = 'consultations'

    id = Column(BigInteger, primary_key=True, index=True)
    created_at = Column(DateTime, nullable=False)
    text = Column(String(200), nullable=False)
    employee_id = Column(Integer, ForeignKey('employees.id'), nullable=False)

    citizen = relationship('Client', back_populates='consultations')
    employee = relationship('Employee', back_populates='consultations')
    
    # TODO: add many-to-many relations with ClientRequest model

