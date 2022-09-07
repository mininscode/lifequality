from sqlalchemy.orm import relationship
from sqlalchemy import Column, BigInteger, String, Boolean, Integer

from database import Base
from database.client_requests.models import ClientRequest
from database.models_associations import association_client_request_with_work_table, \
        association_contractor_with_work_table, \
        association_request_document_with_work_table, \
        association_contract_with_work_table


class Work(Base):
    __tablename__ = 'works'

    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String(150), nullable=False)
    is_emergency = Column(Boolean, nullable=False, default=False)
    duration = Column(Integer, nullable=False)

    contractors = relationship('Contractor', \
            secondary=association_contractor_with_work_table, \
            back_populates='works')

    contracts = relationship('Contract', \
            secondary=association_contract_with_work_table, \
            back_populates='works')

    citizen_requests = relationship('ClientRequest', \
            secondary=association_client_request_with_work_table, \
            back_populates='works')

    requests_documents = relationship('RequestDocument', \
            secondary=association_request_document_with_work_table, \
            back_populates='works')

