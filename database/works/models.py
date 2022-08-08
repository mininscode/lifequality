# from sqlalchemy.orm import relationship
from sqlalchemy import Column, BigInteger, String, Boolean

from database import Base


class Work(Base):
    __tablename__ = 'works'

    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String(150), nullable=False)
    is_emergency = Column(Boolean, nullabel=False, default=False)

    # TODO: add many-to-many relations with model Contractor
    # TODO: add many-to-many relations with model Contract

