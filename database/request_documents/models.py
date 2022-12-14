from sqlalchemy.orm import relationship
from sqlalchemy import Column, BigInteger, ForeignKey, Integer, String, \
                       DateTime

from database import Base
from database.models_associations import  association_request_document_with_work_table


class RequestDocument(Base):
    __tablename__ = 'requests_documents'

    id = Column(BigInteger, primary_key=True, index=True)
    document_type = Column(String(50), nullable=False)
    file_path = Column(String(200), nullable=False)
    created_at = Column(DateTime, nullable=False)
    citizen_request_id = Column(Integer, ForeignKey('citizen_requests.id'), \
                                nullable=False)
    contractor_id = Column(Integer, ForeignKey('contractors.id'), \
                           nullable=False)

    request  = relationship('ClientRequest', back_populates='documents')

    works = relationship('Work', \
            secondary=association_request_document_with_work_table, \
            back_populates='requests_documents')
    
