"""This module contains CRUD methods for database Client model"""

from datetime import date
from sqlalchemy.orm import Session

from database.clients import models, schemas


# CREATE data in database
def create_citizen(db: Session, citizen: schemas.Client):
    db_citizen = models.Client(
        name=citizen.name,
        surname=citizen.surname,
        patronymic=citizen.patronymic,
        house_id=citizen.house_id,
        flat_number=citizen.flat_number,
        is_registered=citizen.is_registered,
        user_id=citizen.user_id
    )
    db.add(db_citizen)
    db.commit()
    db.refresh(db_citizen)
    return db_citizen

def create_citizen_passport(db: Session, passport: schemas.ClientPassport):
    db_passport = models.ClientPassport(
        passport_serial=passport.passport_serial,
        passport_number=passport.passport_number,
        passport_date=passport.passport_date,
        passport_office=passport.passport_office,
        citizen_id=passport.citizen_id,
        is_active=passport.is_active
    )
    db.add(db_passport)
    db.commit()
    db.refresh(db_passport)
    return db_passport

# READ data from database
def get_citizen_by_citizen_id(db: Session, citizen_id: int):
    return db.query(models.Client).filter(models.Client.id == \
           citizen_id).first()

def get_citizen_by_user_id(db: Session, user_id: int):
    return db.query(models.Client).filter(models.Client.user_id == \
           user_id).first()

def get_all_citizens(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Client).offset(skip).limit(limit).all()

def get_citizen_passport_by_citizen_id(db: Session, citizen_id: int):
    return db.query(models.ClientPassport).filter(models.ClientPassport.\
           citizen_id == citizen_id).first()

def get_citizen_all_passports(db: Session, citizen_id: int, skip: int = 0, \
                              limit: int = 100):
    return db.query(models.ClientPassport).filter(models.ClientPassport.\
           citizen_id == citizen_id).offset(skip).limit(limit).all()

def get_all_citizens_passports(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ClientPassport).offset(skip).limit(limit).all()

# UPDATE data in database
def update_citizen_name(db: Session, citizen: schemas.Client, name: str):
    citizen.name = name
    db.commit()
    db.refresh(citizen)
    return citizen

def update_citizen_surname(db: Session, citizen: schemas.Client, surname: str):
    citizen.surname = surname
    db.commit()
    db.refresh(citizen)
    return citizen

def update_citizen_patronymic(db: Session, citizen: schemas.Client, \
                              patronymic: str):
    citizen.patronymic = patronymic
    db.commit()
    db.refresh(citizen)
    return citizen

def update_citizen_house_id(db: Session, citizen: schemas.Client, \
                            house_id: int):
    citizen.house_id = house_id
    db.commit()
    db.refresh(citizen)
    return citizen

def update_citizen_flat_number(db: Session, citizen: schemas.Client, \
                               flat_number: int):
    citizen.flat_number = flat_number
    db.commit()
    db.refresh(citizen)
    return citizen

def update_citizen_is_registered(db: Session, citizen: schemas.Client, \
                                 is_registered: bool):
    citizen.is_registered = is_registered
    db.commit()
    db.refresh(citizen)
    return citizen

def update_citizen_user_id(db: Session, citizen: schemas.Client, user_id: int):
    citizen.user_id = user_id
    db.commit()
    db.refresh(citizen)
    return citizen

def update_citizen_passport_serial(db: Session, serial: str, \
                                   passport: schemas.ClientPassport):
    passport.passport_serial = serial
    db.commit()
    db.refresh(passport)
    return passport

def update_citizen_passport_number(db: Session, number: int, \
                                   passport: schemas.ClientPassport):
    passport.passport_number = number
    db.commit()
    db.refresh(passport)
    return passport

def update_citizen_passport_date(db: Session, passport_date: date, \
                                 passport: schemas.ClientPassport):
    passport.passport_date = passport_date
    db.commit()
    db.refresh(passport)
    return passport

def update_citizen_passport_office(db: Session, office: str, \
                                   passport: schemas.ClientPassport):
    passport.passport_office = office
    db.commit()
    db.refresh(passport)
    return passport

def update_citizen_passport_active_status(db: Session, status: bool, \
                                          passport: schemas.ClientPassport):
    passport.is_active = status
    db.commit()
    db.refresh(passport)
    return passport

# DELETE data from database
def delete_citizen(db: Session, citizen_id: int):
    db_citizen = get_citizen_by_citizen_id(db, citizen_id)
    db.delete(db_citizen)
    db.commit()

def delete_citizen_passport(db: Session, citizen_id: int):
    db_passport = get_citizen_passport_by_citizen_id(db, citizen_id)
    db.delete(db_passport)
    db.commit()

