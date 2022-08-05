# from sqlalchemy.orm import relationship
from sqlalchemy import Column, BigInteger, String

from database import Base


class RequestSource(Base):
    __tablename__ = 'statuses'

    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String(50), nullable=False)

    # requests = relationship('ClientRequest', back_population='source')
