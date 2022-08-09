from sqlalchemy.orm import relationship
from sqlalchemy import Column, BigInteger, ForeignKey, String, Integer, \
                       Boolean, Text, DateTime

from database import Base


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
    record_id = Column(Integer, ForeignKey('call_records.id'), nullable=True)

    citizen = relationship('Client', back_populates='citizen_requests')
    status = relationship('RequestStatus', back_populates='citizen_requests')
    comments = relationship('Comment', back_populates='citizen_request')
    source = relationship('RequestSource', back_populates='citizen_requests')
    record = relationship('CallRecord', back_populates='citizen_requests')
    documents = relationship('RequestDocument', back_populates='request')
    comments = relationship('Comment', back_populates='citizen_request')
    likes =  relationship('Like', back_populates='citizen_request')

    # TODO: add many-to-many relations with Contractor model
    # TODO: add many-to-many relations with Work model
    # TODO: add many-to-manu relations with Employee model
    # TODO: add many-to-many relations with Consultation model
