"""This module contains CRUD methods for the CallRecord model"""

from typing import Literal
from datetime import datetime
from sqlalchemy.orm import Session

from database.call_records import models, schemas


# CREATE date in database
def create_call_record(db: Session, \
        call_record: schemas.CallRecord):
    db_record = models.CallRecord(
        file_path=call_record.file_path,
        created_at=call_record.created_at,
        citizen_id=call_record.citizen_id,
        employee_id=call_record.employee_id
    )
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record

# READ data from database
def get_call_record_by_id(db: Session, record_id: int):
    return db.query(models.CallRecord).filter(\
                    models.CallRecord.id == record_id).first()

def get_call_records_by_create_date(db: Session, created_at: datetime, \
                                    skip: int = 0, limit: int = 100):
    return db.query(models.CallRecord).filter(\
                    models.CallRecord.created_at == \
                    created_at).offset(skip).limit(limit).all()

def get_call_records_by_citizen_id(db: Session, citizen_id: int, \
                                   skip: int = 0, limit: int = 100):
    return db.query(models.CallRecord).filter(\
                    models.CallRecord.citizen_id == \
                    citizen_id).offset(skip).limit(limit).all()

def get_all_records_by_employee_id(db: Session, employee_id: int, \
                                   skip: int = 0, limit: int = 100): 
    return db.query(models.CallRecord).filter(\
                    models.CallRecord.employee_id == \
                    employee_id).offset(skip).limit(limit).all()

def get_all_call_records(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.CallRecord).offset(skip).limit(limit).all()

# UPDATE data in database
def update_call_record_file_path(db: Session, record_id: int, file_path: str):
    db_record = get_call_record_by_id(db, record_id)
    db_record.file_path = file_path
    db.commit()
    db.refresh(db_record)
    return db_record

def update_call_record_create_date(db: Session, record_id: int, \
                                   created_at: datetime):
    db_record = get_call_record_by_id(db, record_id)
    db_record.created_at = created_at
    db.commit()
    db.refresh(db_record)
    return db_record

def update_call_record_citizen_id(db: Session, record_id: int, \
                                  citizen_id: int):
    db_record = get_call_record_by_id(db, record_id)
    db_record.citizen_id = citizen_id
    db.commit()
    db.refresh(db_record)
    return db_record

def update_call_record_employee_id(db: Session, record_id: int, \
                                   employee_id: int):
    db_record = get_call_record_by_id(db, record_id)
    db_record.employee_id = employee_id
    db.commit()
    db.refresh(db_record)
    return db_record

# DELETE data from database
def delete_call_record(db: Session, record_id: int):
    db_record = get_call_record_by_id(db, record_id)
    db.delete(db_record)
    db.commit()

