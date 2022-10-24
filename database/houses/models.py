from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, BigInteger, Integer, String

from database import Base
from database.contracts.models import Contract
from database.house_conditions.models import HouseCondition
from database.meetings.models import Meeting
from database.models_associations import association_contractor_with_house_table


class House(Base):
    __tablename__ = 'houses'

    id = Column(BigInteger, primary_key=True, index=True)
    city = Column(String(100), nullable=False)
    district = Column(String(50), nullable=False)
    street = Column(String(100), nullable=False)
    house_number = Column(String(10), nullable=False)
    condition_id = Column(Integer, ForeignKey('house_conditions.id'), \
                       nullable=False)
    
    condition = relationship('HouseCondition', back_populates='houses')
    
    citizens = relationship('Client', back_populates='house')
    contracts = relationship('Contract', back_populates='house')
    meetings = relationship('Meeting', back_populates='house')

    contractors = relationship('Contractor', \
            secondary=association_contractor_with_house_table, \
            back_populates='houses')

