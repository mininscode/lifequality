from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, BigInteger, String, \
                       Boolean, Date

from database import Base
from database.models_associations import association_meeting_with_client_table


class Client(Base):
    __tablename__ = 'citizens'

    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String(30), nullable=False)
    surname = Column(String(50), nullable=False)
    patronymic = Column(String(50), nullable=True)
    house_id = Column(Integer, ForeignKey('houses.id'), nullable=False)
    flat_number = Column(Integer, nullable=False)
    is_registered = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    
    passports = relationship('ClientPassport', back_populates='citizen')
    house = relationship('House', back_populates='citizens')
    user = relationship('User', back_populates='citizens')
    citizen_requests = relationship('ClientRequest', back_populates='citizen')
    request_records = relationship('CitizenRequestCallRecord', \
                                   back_populates='citizen')
    consultation_records = relationship('ConsultationCallRecord', \
                                        back_populates='citizen')

    meetings = relationship('Meeting', \
            secondary=association_meeting_with_client_table, \
            back_populates='citizens')

    
class ClientPassport(Base):
    __tablename__ = 'citizens_passports'

    id = Column(BigInteger, primary_key=True, index=True)
    passport_serial = Column(String(20), nullable=False)
    passport_number = Column(Integer, nullable=False)
    passport_date = Column(Date, nullable=False)
    passport_office = Column(String(150), nullable=False)
    citizen_id = Column(BigInteger, ForeignKey('citizens.id'), nullable=False)
    is_active = Column(Boolean, default=True)

    citizen = relationship('Client', back_populates='passports')

