from sqlalchemy.orm import relationship
from sqlalchemy import Column, BigInteger, Integer, String, ForeignKey

from database import Base


class Contractor(Base):
    __tablename__ = 'contractors'

    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    contract_id = Column(Integer, ForeignKey('contracts.id'), nullable=False)
    house_id = Column(Integer, ForeignKey('houses.id'), nullable=False)

    house = relationship('House', back_populates='contractors')
    # works = relationship('Work', back_populates='contractor')
    contracts = relationship('Contract', back_populates='contractor')

