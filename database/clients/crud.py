"""This module contains CRUD methods for database Client model"""

from datetime import date
from sqlalchemy.orm import Session

from database.clients import models, schemas


# CREATE data in database
def create_citizen_base(db: Session, citizen: schemas.ClientBase):
    db_citizen = models.Client(
        name=citizen.name,
        surname=citizen.surname,
        patronymic=citizen.patronymic
    )
    db.add(db_citizen)
    db.commit()
    db.refresh(db_citizen)
    return db_citizen

def create_citizen_full(db: Session, citizen: schemas.Client):
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

def create_citizen_passport(db: Session, citizen: cshema.ClientPassport):
    db_passport = models.ClientPassport(
        passport_serial=citizen.passport_serial,
        passport_number=citizen.passport_number,
        passport_date=citizen.passport_date,
        passport_office=citizen.passport_office,
        citizen_id=citizen.citizen_id,
        is_active=citizen.is_active
    )
    db.add(db_passport)
    db.commit()
    db.refresh(db_passport)
    return db_passport

# READ data from database
def get_citizen_by_citizen_id(db: Session, citizen_id: int):
    return db.query(models.Client).filter(models.Client.id == \
           citizen_id).first()

def get_all_citizens(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Client).offset(skip).limit(limit).all()

def get_citizen_passport_by_citizen_id(db: Session, citizen_id: int):
    return db.query(models.ClientPassport).filter(models.ClientPassport.\
           citizen_id == citizen_id).first()

def get_all_citizens_passports(db: Session, citizen_id: int):
    return db.query(models.ClientPassport).filter(models.ClientPassport.\
           citizen_id == citizen_id).all()

# UPDATE data in database
def update_citizen_name(db: Session, citizen_id: int, name: str):
    db_citizen = get_citizen_by_citizen_id(db, citizen_id)
    db_citizen.name = name
    db.commit()
    db.refresh(db_citizen)
    return db_citizen

def update_citizen_surname(db: Session, citizen_id: int, surname: str):
    db_citizen = get_citizen_by_citizen_id(db, citizen_id)
    db_citizen.surname = surname
    db.commit()
    db.refresh(db_citizen)
    return db_citizen

def update_citizen_patronymic(db: Session, citizen_id: int, patronymic: str):
    db_citizen = get_citizen_by_citizen_id(db, citizen_id)
    db_citizen.patronymic = patronymic
    db.commit()
    db.refresh(db_citizen)
    return db_citizen

def update_citizen_house_id(db: Session, citizen_id: int, house_id: int):
    db_citizen = get_citizen_by_citizen_id(db, citizen_id)
    db_citizen.house_id = house_id
    db.commit()
    db.refresh(db_citizen)
    return db_citizen

def update_citizen_flat_number(db: Session, citizen_id: int, flat_number: int):
    db_citizen = get_citizen_by_citizen_id(db, citizen_id)
    db_citizen.flat_number = flat_number
    db.commit()
    db.refresh(db_citizen)
    return db_citizen

def update_citizen_is_registered(db: Session, citizen_id: int, is_registered: bool):
    db_citizen = get_citizen_by_citizen_id(db, citizen_id)
    db_citizen.is_registered = is_registered
    db.commit()
    db.refresh(db_citizen)
    return db_citizen

def update_citizen_user_id(db: Session, citizen_id: int, user_id: int):
    db_citizen = get_citizen_by_citizen_id(db, citizen_id)
    db_citizen.user_id = user_id
    db.commit()
    db.refresh(db_citizen)
    return db_citizen

def update_citizen_passport_serial(db: Session, citizen_id: int, serial: str):
    db_passport = get_citizen_passport_by_citizen_id(db, citizen_id)
    db_passport.passport_serial = serial
    db.commit()
    db.refresh(db_passport)
    return db_passport

def update_citizen_passport_number(db: Session, citizen_id: int, number: int):
    db_passport = get_citizen_passport_by_citizen_id(db, citizen_id)
    db_passport.passport_number = number
    db.commit()
    db.refresh(db_passport)
    return db_passport

def update_citizen_passport_date(db: Session, citizen_id: int, passport_date: date):
    db_passport = get_citizen_passport_by_citizen_id(db, citizen_id)
    db_passport.passport_date = passport_date
    db.commit()
    db.refresh(db_passport)
    return db_passport

def update_citizen_passport_office(db: Session, citizen_id: int, office: str):
    db_passport = get_citizen_passport_by_citizen_id(db, citizen_id)
    db_passport.passport_office = office
    db.commit()
    db.refresh(db_passport)
    return db_passport

def update_citizen_passport_active_status(db: Session, citizen_id: int, status: bool):
    db_passport = get_citizen_passport_by_citizen_id(db, citizen_id)
    db_passport.is_active = status
    db.commit()
    db.refresh(db_passport)
    return db_passport

# DELETE data from database
def delete_citizen(db: Session, citizen_id: int):
    db_citizen = get_citizen_by_citizen_id(db, citizen_id)
    db.delete(db_citizen)
    db.commit()

def delete_citizen_passport(db: Session, citizen_id: int):
    db_passport = get_citizen_passport_by_citizen_id(db, citizen_id)
    db.delete(db_passport)
    db.commit()

