from sqlalchemy.orm import relationship
from sqlalchemy import Column, BigInteger, ForeignKey, Integer, String, Boolean

from database import Base
from database.models_associations import association_client_request_with_contractor_table, \
        association_contractor_with_house_table, \
        association_contractor_with_work_table


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
    
    houses = relationship('House', \
            secondary=association_contractor_with_house_table, \
            back_populates='contractors')

    works = relationship('Work', \
            secondary=association_contractor_with_work_table, \
            back_populates='contractors')

    citizen_requests = relationship('ClientRequest', \
            secondary=association_client_request_with_contractor_table, \
            back_populates='contractors')

