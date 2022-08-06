from sqlalchemy.orm import relationship
from sqlalchemy import Column, BigInteger, Integer, Date, String, ForeignKey

from database import Base


class Contract(Base):
    __tablename__ = 'contracts'

    id = Column(BigInteger, primary_key=True, index=True)
    contract_number = Column(Integer, nullable=True)
    contract_date = Column(Date, nullable=False)
    contract_file = Column(String(250), nullable=False)
    house_id = Column(Integer, ForeignKey('houses.id'), nullable=False)
    contractor_id = Column(Integer, ForeignKey('contractors.id'),\
                           nullable=False)

    house = relationship('House', back_population='contracts')
    contractor = relationship('Contractor', back_population='contracts')
    
