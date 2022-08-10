"""This module contains CRUD methods for the CallRecord model"""

from typing import Literal
from datetime import datetime
from sqlalchemy.orm import Session

from database.call_records import models, schemas


# CREATE date in database
def create_cittizen_request_call_record(db: Session, \
        call_record: schemas.CitizenRequestCallRecord):
    db_record = models.CitizenRequestCallRecord(
        file_path=call_record.file_path,
        created_at=call_record.created_at,
        citizen_id=call_record.citizen_id,
        employee_id=call_record.employee_id,
        citizen_request_id=call_record.citizen_request_id
    )
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record

def create_consultation_call_record(db: Session, \
        call_record: schemas.ConsultationCallRecord):
    db_record = models.ConsultationCallRecord(
        file_path=call_record.file_path,
        created_at=call_record.created_at,
        citizen_id=call_record.citizen_id,
        employee_id=call_record.employee_id,
        consultation_id=call_record.consultation_id
    )
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record

# READ data from database
def get_call_record_by_id(db: Session, \
        request_type: Literal['citizen_request'] | Literal['consultation'], \
        record_id: int):
    if request_type == 'consultation':
        model_object = models.ConsultationCallRecord
    else:
        model_object = models.CitizenRequestCallRecord
    return db.query(model_object).filter(model_object.id == record_id).first()

def get_call_records_by_create_date(db: Session, \
        request_type: Literal['citizen_request'] | Literal['consultation'], \
        created_at: datetime, skip: int = 0, limit: int = 100):
    if request_type == 'consultation':
        model_object = models.ConsultationCallRecord
    else:
        model_object = models.CitizenRequestCallRecord
    return db.query(model_object).filter(model_object.created_at == \
                    created_at).offset(skip).limit(limit).all()

def get_call_records_by_citizen_id(db: Session, 
        request_type: Literal['citizen_request'] | Literal['consultation'], \
        citizen_id: int, skip: int = 0, limit: int = 100):
    
    if request_type == 'consultation':
        model_object = models.ConsultationCallRecord
    else:
        model_object = models.CitizenRequestCallRecord
    return db.query(model_object).filter(model_object.citizen_id == \
                    citizen_id).offset(skip).limit(limit).all()

def get_all_records_by_employee_id(db: Session, \
        request_type: Literal['citizen_request'] | Literal['consultation'], \
        employee_id: int, skip: int = 0, limit: int = 100): 
    if request_type == 'consultation':
        model_object = models.ConsultationCallRecord
    else:
        model_object = models.CitizenRequestCallRecord
    return db.query(model_object).filter(model_object.employee_id == \
                    employee_id).offset(skip).limit(limit).all()

def get_all_call_records_by_request_type(db: Session, \
        request_type: Literal['citizen_request'] | Literal['consultation'], \
        skip: int = 0, limit: int = 100):
    if request_type == 'consultation':
        model_object = models.ConsultationCallRecord
    else:
        model_object = models.CitizenRequestCallRecord
    return db.query(model_object).offset(skip).limit(limit).all()

# UPDATE data in database
def update_call_record_file_path(db: Session, \
        request_type: Literal['citizen_request'] | Literal['consultation'], \
        record_id: int, file_path: str):
    db_record = get_call_record_by_id(db, request_type, record_id)
    db_record.file_path = file_path
    db.commit()
    db.refresh(db_record)
    return db_record

def update_call_record_create_date(db: Session, \
        request_type: Literal['citizen_request'] | Literal['consultation'], \
        record_id: int, created_at: datetime):
    db_record = get_call_record_by_id(db, request_type, record_id)
    db_record.created_at = created_at
    db.commit()
    db.refresh(db_record)
    return db_record

def update_call_record_citizen_id(db: Session, \
        request_type: Literal['citizen_request'] | Literal['consultation'], \
        record_id: int, citizen_id: int):
    db_record = get_call_record_by_id(db, request_type, record_id)
    db_record.citizen_id = citizen_id
    db.commit()
    db.refresh(db_record)
    return db_record

def update_call_record_employee_id(db: Session, \
        request_type: Literal['citizen_request'] | Literal['consultation'], \
        record_id: int, employee_id: int):
    db_record = get_call_record_by_id(db, request_type, record_id)
    db_record.employee_id = employee_id
    db.commit()
    db.refresh(db_record)
    return db_record

# DELETE data from database
def delete_call_record(db: Session, \
        request_type: Literal['citizen_request'] | Literal['consultation'], \
        record_id: int):
    db_record = get_call_record_by_id(db, request_type, record_id)
    db.delete(db_record)
    db.commit()

