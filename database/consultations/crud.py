"""This module contains CRUD operations for the Consultation model"""

from datetime import datetime
from sqlalchemy.orm import Session

from database.consultations import models, schemas


# CREATE data in database
def create_consultation(db: Session, consultation: schemas.Consultation):
    db_consultation = models.Consultation(
        created_at=consultation.created_at,
        text=consultation.text,
        employee_id=consultation.employee_id,
        record_id=consultation.record_id
    )
    db.add(db_consultation)
    db.commit()
    db.refresh(db_consultation)
    return db_consultation

# READ data from database
def get_consultation_by_id(db: Session, consultation_id: int):
    return db.query(models.Consultation).filter(\
                    models.Consultation.id == consultation_id).first()

def get_coonsultation_by_text(db: Session, text: str):
    return db.query(models.Consultation).filter(\
                    models.Consultation.text == text).first()

def get_consultation_by_record_id(db: Session, record_id: int):
    return db.query(models.Consultation).filter(\
                    models.Consultation.record_id == record_id).first()

def get_consultations_by_crate_date(db: Session, created_at: datetime, \
                                    skip: int = 0, limit: int = 100):
    return db.query(models.Consultation).filter(\
                    models.Consultation.created_at == \
                    created_at).offset(skip).limit(limit).all()

def get_consultations_by_employee_id(db: Session, employee_id: int, \
                                     skip: int = 0, limit: int = 100):
    return db.query(models.Consultation).filter(\
                    models.Consultation.employee_id == \
                    employee_id).offset(skip).limit(limit).all()

def get_all_consultations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Consultation).offset(skip).limit(limit).all()

# UPDATE data in database
def update_consultation_create_date(db: Session, consultation_id: int, \
                                    created_at: datetime):
    db_consultation = get_consultation_by_id(db, consultation_id)
    db_consultation.created_at = created_at
    db.commit()
    db.refresh(db_consultation)
    return db_consultation

def update_consultation_text(db: Session, consultation_id: int, text: str):
    db_consultation = get_consultation_by_id(db, consultation_id)
    db_consultation.text = text
    db.commit()
    db.refresh(db_consultation)
    return db_consultation

def update_consultation_employee_id(db: Session, consultation_id: int, \
                                    employee_id: int):
    db_consultation = get_consultation_by_id(db, consultation_id)
    db_consultation.employee_id = employee_id
    db.commit()
    db.refresh(db_consultation)
    return db_consultation

def update_consultation_record_id(db: Session, consultation_id: int, \
                                  record_id: int):
    db_consultation = get_consultation_by_id(db, consultation_id)
    db_consultation.record_id = record_id
    db.commit()
    db.refresh(db_consultation)
    return db_consultation

# DELETE data from database
def delete_consultation(db:Session, consultation_id: int):
    db_consultation = get_consultation_by_id(db, consultation_id)
    db.delete(db_consultation)
    db.commit()
    db.refresh(db_consultation)
    return db_consultation

