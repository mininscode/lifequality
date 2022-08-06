# from sqlalchemy.orm import relationship
from sqlalchemy import Column, BigInteger, Integer, String, ForeignKey

from database import Base


class Contractor(Base):
    __tablename__ = 'contractors'

    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    contract = Column(Integer, ForeignKey('contracts.id'), nullable=False)
    house = Column(Integer, ForeignKey('houses.id'), nullable=False)

    # houses = relationship('House', back_populates='contractor')
    # works = relationship('Work', back_populates='contractor')
    # contract = relationship('Contract', back_populates='contractor')

