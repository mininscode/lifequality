from sqlalchemy.orm import relationship
from sqlalchemy import Column, BigInteger, ForeignKey, Integer, String, Boolean

from database import Base


class Contractor(Base):
    __tablename__ = 'contractors'

    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    city = Column(String(100), nullable=False)
    street = Column(String(100), nullable=False)
    building = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    is_emergency_service = Column(Boolean, nullable=False, default=False)

    contracts = relationship('Contract', back_populates='contractor')
    user = relationship('User', back_populates='contractors')
    
    # TODO: add many-to-many relations with model House
    # TODO: add many-to-many relations with model Work

