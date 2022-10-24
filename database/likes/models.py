from sqlalchemy.orm import relationship
from sqlalchemy import Column, BigInteger, ForeignKey, Integer, String, \
                       DateTime

from database import Base


class Like(Base):
    __tablename__ = 'likes'

    id = Column(BigInteger, primary_key=True, index=True)
    citizen_request_id = Column(Integer, ForeignKey('citizen_requests.id'), \
                                nullable=False)
    count = Column(Integer, nullable=False)
    author_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    created_at = Column(DateTime, nullable=False)

    citizen_request = relationship('ClientRequest', back_populates='likes')
    user = relationship('User', back_populates='likes')

