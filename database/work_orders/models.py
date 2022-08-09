from sqlalchemy.orm import relationship
from sqlalchemy import Column, BigInteger, ForeignKey, Integer, String, \
                       DateTime

from database import Base


class WorkOrder(Base):
    __tablename__ = 'work_orders'

    id = Column(BigInteger, primary_key=True, index=True)
    file_path = Column(String(200), nullable=False)
    created_at = Column(DateTime, nullable=False)
    citizen_request_id = Column(Integer, ForeignKey('client_requests.id'), \
                                nullable=False)
    contractor_id = Column(Integer, ForeignKey('contractors.id'), \
                           nullable=False)

    request  = relationship('ClientRequest', back_populates='work_orders')

    # TODO: add many-to-many relations with Work model
    
