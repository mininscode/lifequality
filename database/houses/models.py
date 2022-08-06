from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, BigInteger, Integer, String

from database import Base


class House(Base):
    __tablename__ = 'houses'

    id = Column(BigInteger, primary_key=True, index=True)
    city = Column(String(100), nullable=False)
    district = Column(String(50), nullable=False)
    street = Column(String(100), nullable=False)
    house_number = Column(Integer, nullable=False)
    condition_id = Column(Integer, ForeignKey('house_conditions.id'), \
                       nullable=False)
    
    citizens = relationship('Client', back_populates='house')
    conditions = relationship('HouseCondition', back_populates='conditions')

