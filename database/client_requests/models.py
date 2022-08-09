from sqlalchemy.orm import relationship
from sqlalchemy import Column, BigInteger, ForeignKey, String, Integer, \
                       Boolean, Text, DateTime

from database import Base


class ClientRequest(Base):
    __tablename__ = 'citizen_requests'

    id = Column(BigInteger, primary_key=True, index=True)
    text = Column(Text, nullable=False)
    citizen_id = Column(Integer, ForeignKey('clients.id'), nullable=False)
    address = Column(String(200), nullable=False)
    request_source = Column(String(50), ForeignKey('request_sources.name'), \
                            nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    closed_at = Column(DateTime, nullable=True)
    planed_duration = Column(DateTime, ForeignKey('works.duration'), \
                             nullable=False)
    fact_duration = Column(DateTime, nullable=False)
    request_status = Column(String(50), ForeignKey('request_statuses.name'), \
                            nullable=False)
    citizen_feedback = Column(String(200), nullable=True)
    is_active = Column(Boolean, nullable=False, default=True)
    record_id = Column(Integer, ForeignKey('call_records.id'), nullable=True)

    citizen = relationship('Client', back_populates='citizen_requests')
    status = relationship('RequestStatus', back_populates='citizen_requests')
    comments = relationship('Comment', back_populates='citizen_request')
    source = relationship('RequestSource', back_populates='citizen_requests')
    record = relationship('CallRecord', back_populates='client_requests')
    work_orders = relationship('WorkOrder', back_populates='request')

    # TODO: add many-to-many relations with Contractor model
    # TODO: add many-to-many relations with Work model
    # TODO: add many-to-manu relations with Employee model
    # TODO: add many-to-many relations with Consultation model
