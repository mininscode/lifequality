"""This module contains CRUD methods for database House model"""

from sqlalchemy.orm import Session

from database.houses import models, schemas
from validation_types import AddressType


# CREATE data in database
def create_house(db: Session, house: schemas.House):
    db_house = models.House(
        city=house.city,
        district=house.district,
        street=house.street,
        house_number=house.house_number,
        condition=house.condition
    )
    db.add(db_house)
    db.commit()
    db.refresh(db_house)
    return db_house

# READ data from database
def get_house_by_address(db: Session, address: AddressType):
    city = address['city']
    district = address['district']
    street = address['street']
    house_number = address['house_number']
    return db.query(models.House).filter(\
           models.House.city == city).filter(\
           models.House.district == district).filter(\
           models.House.street == street).filter(\
           models.House.house_number == house_number).first()

def get_all_houses_by_city(db: Session, city: str):
    return db.query(models.House).filter(models.House.city == city).all()

def get_all_houses_by_district(db: Session, district: str):
    return db.query(models.House).filter(models.House.district == \
           district).all()

def get_all_houses_by_street(db: Session, street: str):
    return db.query(models.House).filter(models.House.street == street).all()

def get_all_houses_by_house_number(db: Session, house_number: int):
    return db.query(models.House).filter(models.House.house_number == \
           house_number).all()

def get_all_houses_by_condition(db: Session, condition: str):
    return db.query(models.House).filter(models.House.condition == \
           condition).first()

def get_all_houses(db: Session):
    return db.query(models.House).all()

# UPDATE data in database
def update_house_city(db: Session, address: AddressType, city: str):
    db_house = get_house_by_address(db, address)
    db_house.city = city
    db.commit()
    db.refresh(db_house)
    return db_house

def update_house_disctrict(db: Session, address: AddressType, district: str):
    db_house = get_house_by_address(db, address)
    db_house.district = district
    db.commit()
    db.refresh(db_house)
    return db_house

def update_house_street(db: Session, address: AddressType, street: str):
    db_house = get_house_by_address(db, address)
    db_house.street = street
    db.commit()
    db.refresh(db_house)
    return db_house

def update_house_house_number(db: Session, address: AddressType, house_number: int):
    db_house = get_house_by_address(db, address)
    db_house.house_number = house_number
    db.commit()
    db.refresh(db_house)
    return db_house

def update_house_condition(db: Session, address: AddressType, condition: str):
    db_house = get_house_by_address(db, address)
    db_house.condition = condition
    db.commit()
    db.refresh(db_house)
    return db_house

# DELETE data from database
def delete_house(db: Session, address: AddressType):
    db_house = get_house_by_address(db, address)
    db.delete(db_house)
    db.commit()

