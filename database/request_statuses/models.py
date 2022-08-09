from sqlalchemy.orm import relationship
from sqlalchemy import Column, BigInteger, String

from database import Base


class RequestStatus(Base):
    __tablename__ = 'request_statuses'

    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String(100), nullable=False)

    citizen_requests = relationship('ClientRequest', back_populates='status')

