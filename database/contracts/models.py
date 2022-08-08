from sqlalchemy.orm import relationship
from sqlalchemy import Column, BigInteger, ForeignKey, Integer, Boolean, Date

from database import Base


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

    # TODO: add many-to-many relations with model Contract

