"""This module contains CRUD methods for the Contract model"""

from datetime import date
from sqlalchemy.orm import Session

from database.contracts import models, schemas


# CREATE data in database
def create_contract(db: Session, contract: schemas.Contract):
    db_contract = models.Contract(
        contract_number=contract.contract_number,
        contract_date=contract.contract_date,
        contract_file=contract.contract_file,
        house_id=contract.house_id,
        contractor_id=contract.contractor_id
    )
    db.add(db_contract)
    db.commit()
    db.refresh(db_contract)
    return db_contract

# READ data from database
def get_contract_by_number(db: Session, number: int):
    return db.query(models.Contract).filter(\
                    models.Contract.contract_number == number).first()

def get_contracts_by_date(db: Session, contract_date: date):
    return db.query(models.Contract).filter(\
                    models.Contract.contract_date == contract_date).all()

def get_contracts_by_house_id(db: Session, house_id: int):
    return db.query(models.Contract).filter(\
                    models.Contract.house_id == house_id).all()

def get_contracts_by_contractor_id(db: Session, contractor_id: int):
    return db.query(models.Contract).filter(\
                    models.Contract.contractor_id == contractor_id).all()

def get_all_contracts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Contract).offset(skip).limit(limit).all()

# UPDATE data in database
def update_contract_number(db: Session, number_current: int, number_new: int):
    db_contract = get_contract_by_number(db, number_current)
    db_contract.contract_number = number_new
    db.commit()
    db.refresh(db_contract)
    return db_contract

def update_contract_date(db: Session, number: int, new_date: date):
    db_contract = get_contract_by_number(db, number)
    db_contract.contract_date = new_date
    db.commit()
    db.refresh(db_contract)
    return db_contract

def update_contract_file(db: Session, number: int, file: str):
    db_contract = get_contract_by_number(db, number)
    db_contract.contract_file = file
    db.commit()
    db.refresh(db_contract)
    return db_contract

def update_contract_house_id(db: Session, number: int, house_id: int):
    db_contract = get_contract_by_number(db, number)
    db_contract.house_id = house_id
    db.commit()
    db.refresh(db_contract)
    return db_contract

def update_contract_contractor_id(db: Session, number: int, \
                                     contractor_id: int):
    db_contract = get_contract_by_number(db, number)
    db_contract.contractor_id = contractor_id
    db.commit()
    db.refresh(db_contract)
    return db_contract

# DELETE data from database
def delete_contract(db: Session, number: int):
    db_contract = get_contract_by_number(db, number)
    db.delete(db_contract)
    db.commit()

