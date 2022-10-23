"""This module contains CRUD operations for the Contract model"""

from datetime import date
from sqlalchemy.orm import Session

from database.contracts import models, schemas


# CREATE data in database
def create_contract(db: Session, contract: schemas.Contract):
    db_contract = models.Contract(
        contract_number=contract.contract_number,
        contract_date=contract.contract_date,
        expiration_date=contract.expiration_date,
        contractor_id=contract.contractor_id,
        house_id=contract.house_id,
        is_active=contract.is_active
    )
    db.add(db_contract)
    db.commit()
    db.refresh(db_contract)
    return db_contract

# READ data from database
def get_contract_by_id(db: Session, contract_id: int):
    return db.query(models.Contract).filter(\
                    models.Contract.id == contract_id).first()

def get_contract_by_contract_number(db: Session, contract_number: int):
    return db.query(models.Contract).filter(\
                    models.Contract.contract_number == contract_number).first()

def get_contracts_by_contract_date(db: Session, contract_date: date, \
                                   skip: int = 0, limit: int = 100):
    return db.query(
            models.Contract).filter(\
            models.Contract.contract_date == \
            contract_date).offset(skip).limit(limit).all()

def get_contracts_by_expiration_date(db: Session, expiration_date: date, \
                                    skip: int = 0, limit: int = 100):
    return db.query(models.Contract).filter(\
            models.Contract.expiration_date == \
            expiration_date).offset(skip).limit(limit).all()

def get_contracts_by_contractor_id(db: Session, contractor_id: int, \
                                   skip: int = 0, limit: int = 100):
    return db.query(models.Contract).filter(\
            models.Contract.contractor_id == \
            contractor_id).offset(skip).limit(limit).all()

def get_contracts_by_house_id(db: Session, house_id: int, skip: int = 0, \
                              limit: int = 100):
    return db.query(models.Contract).filter(\
            models.Contract.house_id == \
            house_id).offset(skip).limit(limit).all()

def get_contracts_by_active_status(db: Session, is_active: bool, \
                                   skip: int = 0, limit: int = 100):
    return db.query(models.Contract).filter(\
            models.Contract.is_active == \
            is_active).offset(skip).limit(limit).all()

def get_all_contracts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Contract).offset(skip).limit(limit).all()

# UPDATE data in database
def update_contract_number(db: Session, contract: schemas.Contract, \
                           new_contract_number: int):
    contract.contract_number = new_contract_number
    db.commit()
    db.refresh(contract)
    return contract

def update_contract_contract_date(db: Session, contract: schemas.Contract, \
                                  new_contract_date: date):
    contract.contract_date = new_contract_date
    db.commit()
    db.refresh(contract)
    return contract

def update_contract_expiration_date(db: Session, contract: schemas.Contract, \
                                    new_expiration_date: date):
    contract.expiration_date = new_expiration_date
    db.commit()
    db.refresh(contract)
    return contract

def update_contract_contractor_id(db: Session, contract: schemas.Contract, \
                                  new_contractor_id: int):
    contract.contractor_id = new_contractor_id
    db.commit()
    db.refresh(contract)
    return contract

def update_contract_house_id(db: Session, contract: schemas.Contract, \
                             new_house_id: int):
    contract.house_id = new_house_id
    db.commit()
    db.refresh(contract)
    return contract

def update_contract_active_status(db: Session, contract: schemas.Contract, \
                                  status: bool):
    contract.is_active = status
    db.commit()
    db.refresh(contract)
    return contract

# DELETE data from database
def delete_contract(db: Session, contract_id: int):
    db_contract = get_contract_by_id(db, contract_id)
    db.delete(db_contract)
    db.commit()

