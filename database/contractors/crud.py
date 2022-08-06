"""This module contains CRUD operations for Contractor model"""

from sqlalchemy.orm import Session

from database.contractors import models, schemas


# CREATE data in databse
def create_contractor(db: Session, contractor: schemas.Contractor):
    db_contractor = models.Contractor(
        name = contractor.name,
        contract = contractor.contract,
        house = contractor.house
    )
    db.add(db_contractor)
    db.commit()
    db.refresh(db_contractor)
    return db_contractor

# READ data from database
def get_contractor_by_name(db: Session, name: str):
    return db.query(models.Contractor).filter(\
                    models.Contractor.name == name).first()

def get_all_contractors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Contractor).offset(skip).limit(limit).all()

# UPDATE data in database
def update_contractor_name(db: Session, name_current: str, name_new: str):
    db_contractor = get_contractor_by_name(db, name_current)
    db_contractor.name = name_new
    db.commit()
    db.refresh(db_contractor)
    return db_contractor

def update_contracttor_contract(db: Session, name: str, contract: int):
    db_contractor = get_contractor_by_name(db, name)
    db_contractor.contract = contract
    db.commit()
    db.refresh(db_contractor)
    return db_contractor

def update_contractor_house(db: Session, name: str, house: int):
    db_contractor = get_contractor_by_name(db, name)
    db_contractor.house = house
    db.commit()
    db.refresh(db_contractor)
    return db_contractor

# DALETE date from database
def delete_contractor(db: Session, name: str):
    db_contractor = get_contractor_by_name(db, name)
    db.delete(db_contractor)
    db.commit()

