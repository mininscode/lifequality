from sqlalchemy.orm import relationship
from sqlalchemy import Column, BigInteger, String

from database import Base


class RequestSource(Base):
    __tablename__ = 'request_sources'

    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String(50), nullable=False)

    citizen_requests = relationship('ClientRequest', back_population='source')
