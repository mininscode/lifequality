from sqlalchemy.orm import relationship
from sqlalchemy import Column, BigInteger, ForeignKey, Integer, Boolean, Date

from database import Base
from database.works.models import Work
from database.models_associations import association_contract_with_work_table


class Contract(Base):
    __tablename__ = 'contracts'

    id = Column(BigInteger, primary_key=True, index=True)
    contract_number = Column(Integer, nullable=True)
    contract_date = Column(Date, nullable=False)
    expiration_date = Column(Date, nullable=False)
    contractor_id = Column(Integer, ForeignKey('contractors.id'), \
                                                nullable=False)
    house_id = Column(Integer, ForeignKey('houses.id'), nullable=False)
    is_active = Column(Boolean, nullable=False, default=True)

    contractor = relationship('Contractor', back_populates='contracts')
    house = relationship('House', back_populates='contracts')

    works = relationship('Work', \
            secondary=association_contract_with_work_table, \
            back_populates='contracts')

