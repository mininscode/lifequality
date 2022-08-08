"""This module contains CRUD operations for Contractor model"""

from sqlalchemy.orm import Session

from database.contractors import models, schemas


# CREATE data in database
def create_contractor(db: Session, contractor: schemas.Contractor):
    db_contractor = models.Contractor(
        name=contractor.name,
        city=contractor.city,
        street=contractor.street,
        building=contractor.building,
        contract_id=contractor.contract_id,
        user_id=contractor.user_id
    )
    db.add(db_contractor)
    db.commit()
    db.refresh(db_contractor)
    return db_contractor

# READ data from database
def get_contractor_by_id(db: Session, contractor_id: int):
    return db.query(models.Contractor).filter(\
                    models.Contractor.id == contractor_id).first()

def get_contractor_by_name(db: Session, contractor_name: str):
    return db.query(models.Contractor).filter(\
                    models.Contractor.name == contractor_name).first()

def get_contractor_by_contract_id(db: Session, contract_id: int):
    return db.query(models.Contractor).filter(\
                    models.Contractor.contract_id == contract_id).first()

def get_contractor_by_user_id(db: Session, user_id: int):
    return db.query(models.Contractor).filter(\
                    models.Contractor.user_id == user_id).first()

# UPDATE data in database
def update_contractor_name(db: Session, contractor_id: int, new_name: str):
    db_contractor = get_contractor_by_id(db, contractor_id)
    db_contractor.name = new_name
    db.commit()
    db.refresh(db_contractor)
    return db_contractor

def update_contractor_city(db: Session, contractor_id: int, new_city: str):
    db_contractor = get_contractor_by_id(db, contractor_id)
    db_contractor.city = new_city
    db.commit()
    db.refresh(db_contractor)
    return db_contractor

def update_contractor_street(db: Session, contractor_id: int, \
                             new_street: str):
    db_contractor = get_contractor_by_id(db, contractor_id)
    db_contractor.street = new_street
    db.commit()
    db.refresh(db_contractor)
    return db_contractor

def update_contractor_building(db: Session, contractor_id: int, \
                               new_building: int):
    db_contractor = get_contractor_by_id(db, contractor_id)
    db_contractor.building = new_building
    db.commit()
    db.refresh(db_contractor)
    return db_contractor

def update_contractor_contract_id(db: Session, contractor_id: int, \
                                  new_contract_id: int):
    db_contractor = get_contractor_by_id(db, contractor_id)
    db_contractor.contract_id = new_contract_id
    db.commit()
    db.refresh(db_contractor)
    return db_contractor

def update_contractor_user_id(db: Session, contractor_id: int, \
                              new_user_id: int):
    db_contractor = get_contractor_by_id(db, contractor_id)
    db_contractor.user_id = new_user_id
    db.commit()
    db.refresh(db_contractor)
    return db_contractor

# DELETE data from database
def delete_contractor(db: Session, contractor_id: int):
    db_contractor = get_contractor_by_id(db, contractor_id)
    db.delete(db_contractor)
    db.commit()

