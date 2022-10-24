"""This module contains CRUD methods for database House model"""

from sqlalchemy.orm import Session

from database.houses import models, schemas


# CREATE data in database
def create_house(db: Session, house: schemas.House):
    db_house = models.House(
        city=house.city,
        district=house.district,
        street=house.street,
        house_number=house.house_number,
        condition_id=house.condition_id
    )
    db.add(db_house)
    db.commit()
    db.refresh(db_house)
    return db_house

# READ data from database
def get_house_by_id(db: Session, house_id: int):
    return db.query(models.House).filter(\
           models.House.id == house_id).first()

def get_houses_by_city(db: Session, city: str, skip: int = 0, \
                       limit: int = 100):
    return db.query(models.House).filter(\
                    models.House.city == city).offset(\
                    skip).limit(limit).all()

def get_houses_by_district(db: Session, district: str, skip: int = 0, \
                           limit: int = 100):
    return db.query(models.House).filter(\
                    models.House.district == district).offset(\
                    skip).limit(limit).all()

def get_houses_by_street(db: Session, street: str, skip: int = 0, \
                         limit: int = 100):
    return db.query(models.House).filter(\
                    models.House.street == street).offset(\
                    skip).limit(limit).all()

def get_houses_by_house_number(db: Session, house_number: str, \
                               skip: int = 0, limit: int = 100):
    return db.query(models.House).filter(\
                    models.House.house_number == house_number).offset(\
                    skip).limit(limit).all()

def get_houses_by_condition_id(db: Session, condition_id: int, skip: int = 0, \
                               limit: int = 100):
    return db.query(models.House).filter(\
                    models.House.condition_id == condition_id).offset(\
                    skip).limit(limit).all()

def get_all_houses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.House).offset(skip).limit(limit).all()

# UPDATE data in database
def update_house_city(db: Session, house: schemas.House, city: str):
    house.city = city
    db.commit()
    db.refresh(house)
    return house

def update_house_district(db: Session, house: schemas.House, district: str):
    house.district = district
    db.commit()
    db.refresh(house)
    return house

def update_house_street(db: Session, house: schemas.House, street: str):
    house.street = street
    db.commit()
    db.refresh(house)
    return house

def update_house_house_number(db: Session, house: schemas.House, \
                              house_number: str):
    house.house_number = house_number
    db.commit()
    db.refresh(house)
    return house

def update_house_condition_id(db: Session, house: schemas.House, \
                              condition_id: int):
    house.condition_id = condition_id
    db.commit()
    db.refresh(house)
    return house

# DELETE data from database
def delete_house(db: Session, house_id: int):
    db_house = get_house_by_id(db, house_id)
    db.delete(db_house)
    db.commit()

