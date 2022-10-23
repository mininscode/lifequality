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
        user_id=contractor.user_id,
        is_emergency_service=contractor.is_emergency_service
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

def get_contractor_by_user_id(db: Session, user_id: int):
    return db.query(models.Contractor).filter(\
                    models.Contractor.user_id == user_id).first()

def get_contractors_by_emergency_service_status(db: Session, \
                                               emergency_status: bool, \
                                               skip: int = 0, \
                                               limit: int = 100):
    return db.query(models.Contractor).filter(\
                    models.Contractor.is_emergency_service == \
                    emergency_status).offset(skip).limit(limit).all()

def get_all_contractors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Contractor).offset(skip).limit(limit).all()

# UPDATE data in database
def update_contractor_name(db: Session, contractor: schemas.Contractor, \
                           new_name: str):
    contractor.name = new_name
    db.commit()
    db.refresh(contractor)
    return contractor

def update_contractor_city(db: Session, contractor: schemas.Contractor, \
                           new_city: str):
    contractor.city = new_city
    db.commit()
    db.refresh(contractor)
    return contractor

def update_contractor_street(db: Session, contractor: schemas.Contractor, \
                             new_street: str):
    contractor.street = new_street
    db.commit()
    db.refresh(contractor)
    return contractor

def update_contractor_building(db: Session, contractor: schemas.Contractor, \
                               new_building: int):
    contractor.building = new_building
    db.commit()
    db.refresh(contractor)
    return contractor

def update_contractor_contract_id(db: Session, \
                                  contractor: schemas.Contractor, \
                                  new_contract_id: int):
    contractor.contract_id = new_contract_id
    db.commit()
    db.refresh(contractor)
    return contractor

def update_contractor_user_id(db: Session, contractor: schemas.Contractor, \
                              new_user_id: int):
    contractor.user_id = new_user_id
    db.commit()
    db.refresh(contractor)
    return contractor

def update_contractor_emergency_status(db: Session, \
                                       contractor: schemas.Contractor, \
                                       new_emergency_status: bool):
    contractor.is_emegrency_service = new_emergency_status
    db.commit()
    db.refresh(contractor)
    return contractor

# DELETE data from database
def delete_contractor(db: Session, contractor_id: int):
    db_contractor = get_contractor_by_id(db, contractor_id)
    db.delete(db_contractor)
    db.commit()

