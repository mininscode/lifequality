from sqlalchemy.orm import relationship
from sqlalchemy import Column, BigInteger, ForeignKey, Integer, String, \
                       DateTime

from database import Base


class CallRecord(Base):
    __tablename__ = 'call_records'
    
    id = Column(BigInteger, primary_key=True, index=True)
    file_path = Column(String(200), nullable=False)
    created_at = Column(DateTime, nullable=False)
    citizen_id = Column(Integer, ForeignKey('citizens.id'), nullable=False)
    employee_id = Column(Integer, ForeignKey('employees.id'), nullable=False)
    citizen_request_id = Column(Integer, ForeignKey('citizen_requests.id'), \
                                nullable=False)

    citizen = relationship('Client', back_populates='records')
    employee = relationship('Employee', back_populates='records')
    citizen_request = relationship('ClientRequest', back_populates='record')
    
