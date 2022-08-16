from sqlalchemy.orm import relationship
from sqlalchemy import Column, BigInteger, Integer, Date, String, Boolean, \
                       ForeignKey

from database import Base
from database.models_associations import association_meeting_with_client_table


class Meeting(Base):
    __tablename__ = 'meetings'

    id =  Column(BigInteger, primary_key=True, index=True)
    meeting_date = Column(Date, nullable=False)
    house_id = Column(Integer, ForeignKey('houses.id'), nullable=False)
    is_legal = Column(Boolean, nullable=False)
    meeting_record = Column(String, nullable=False)

    house = relationship('House', back_populates='meetings')

    citizens = relationship('Client', \
            secondary=association_meeting_with_client_table,
            back_populates='meetings')

