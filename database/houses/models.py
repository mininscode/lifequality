from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, BigInteger, Integer, String

from database import Base
from database.models_associations import association_contractor_with_house_table


class House(Base):
    __tablename__ = 'houses'

    id = Column(BigInteger, primary_key=True, index=True)
    city = Column(String(100), nullable=False)
    district = Column(String(50), nullable=False)
    street = Column(String(100), nullable=False)
    house_number = Column(Integer, nullable=False)
    condition_id = Column(Integer, ForeignKey('house_conditions.id'), \
                       nullable=False)
    
    condition = relationship('HouseCondition', back_populates='houses')
    
    citizens = relationship('Client', back_populates='house')
    contracts = relationship('Contracts', back_populates='house')
    meetings = relationship('Meeting', back_populates='house')

    contractors = relationship('Contractor', \
            secondary=association_contractor_with_house_table, \
            back_populates='houses')

