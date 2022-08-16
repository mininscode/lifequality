from sqlalchemy.orm import relationship
from sqlalchemy import Column, BigInteger, ForeignKey, String, Integer, \
                       Boolean, Text, DateTime

from database import Base
from database.models_associations import association_client_request_with_contractor_table, \
        association_client_request_with_work_table, \
        association_client_request_with_employee_table, \
        association_client_request_with_consultation_table


class ClientRequest(Base):
    __tablename__ = 'citizen_requests'

    id = Column(BigInteger, primary_key=True, index=True)
    text = Column(Text, nullable=False)
    citizen_id = Column(Integer, ForeignKey('citizens.id'), nullable=False)
    address = Column(String(200), nullable=False)
    request_source = Column(Integer, ForeignKey('request_sources.id'), \
                            nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    closed_at = Column(DateTime, nullable=True)
    fact_duration = Column(DateTime, nullable=False)
    request_status = Column(Integer, ForeignKey('request_statuses.id'), \
                            nullable=False)
    citizen_feedback = Column(String(200), nullable=True)
    is_active = Column(Boolean, nullable=False, default=True)

    citizen = relationship('Client', back_populates='citizen_requests')
    status = relationship('RequestStatus', back_populates='citizen_requests')
    source = relationship('RequestSource', back_populates='citizen_requests')
    
    record = relationship('CallRecord', back_populates='citizen_request', \
                          uselist=False)
    
    comments = relationship('Comment', back_populates='citizen_request')
    documents = relationship('RequestDocument', back_populates='request')
    comments = relationship('Comment', back_populates='citizen_request')
    likes =  relationship('Like', back_populates='citizen_request')

    contractors = relationship('Conractor', \
            secondary=association_client_request_with_contractor_table, \
            back_populates='citizen_requests')

    works = relationship('Work', \
            secondary=association_client_request_with_work_table, \
            back_populates='citizen_requests')

    employees = relationship('Employee', \
            secondary=association_client_request_with_employee_table, \
            back_populates='citizen_requests')

    consultations = relationship('Consultation', \
            secondary=association_client_request_with_consultation_table, \
            back_populates='citizen_requests')

