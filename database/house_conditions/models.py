from sqlalchemy.orm import relationship
from sqlalchemy import Column, BigInteger, String

from database import Base


class HouseCondition(Base):
    __tablename__ = 'house_conditions'

    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String(50), nullable=False)

    house = relationship('House', back_populates='condition')

