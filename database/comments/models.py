from sqlalchemy.orm import relationship
from sqlalchemy import Column, BigInteger, Integer, ForeignKey, String, \
                       DateTime

from database import Base


class Comment(Base):
    __tablename__ = 'citizen_comments'

    id = Column(BigInteger, primary_key=True, index=True)
    text = Column(String(250), nullable=False)
    author_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    created_at = Column(DateTime, nullable=False)
    citizen_request_id = Column(Integer, ForeignKey('citizen_requests.id'), \
                                nullable=False)

    user = relationship('User', back_populates='comments')
    citizen_request = relationship('ClientRequest', \
                                   back_populates='comments')

