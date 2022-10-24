"""This module contains CRUD operations for the Consultation model"""

from datetime import datetime
from sqlalchemy.orm import Session

from database.consultations import models, schemas


# CREATE data in database
def create_consultation(db: Session, consultation: schemas.Consultation):
    db_consultation = models.Consultation(
        created_at=consultation.created_at,
        text=consultation.text,
        citizen_id=consultation.citizen_id
    )
    db.add(db_consultation)
    db.commit()
    db.refresh(db_consultation)
    return db_consultation

# READ data from database
def get_consultation_by_id(db: Session, consultation_id: int):
    return db.query(models.Consultation).filter(\
                    models.Consultation.id == consultation_id).first()

def get_consultations_by_create_date(db: Session, created_at: datetime, \
                                    skip: int = 0, limit: int = 100):
    return db.query(models.Consultation).filter(\
                    models.Consultation.created_at == \
                    created_at).offset(skip).limit(limit).all()

def get_consultations_by_citizen_id(db: Session, citizen_id: int, \
                                     skip: int = 0, limit: int = 100):
    return db.query(models.Consultation).filter(\
                    models.Consultation.citizen_id == \
                    citizen_id).offset(skip).limit(limit).all()

def get_all_consultations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Consultation).offset(skip).limit(limit).all()

# UPDATE data in database
def update_consultation_create_date(db: Session, \
                                    consultation: schemas.Consultation, \
                                    created_at: datetime):
    consultation.created_at = created_at
    db.commit()
    db.refresh(consultation)
    return consultation

def update_consultation_text(db: Session, \
                             consultation: schemas.Consultation, \
                             new_text: str):
    consultation.text = new_text
    db.commit()
    db.refresh(consultation)
    return consultation

def update_consultation_citizen_id(db: Session, \
                                    consultation: schemas.Consultation, \
                                    citizen_id: int):
    consultation.citizen_id = citizen_id
    db.commit()
    db.refresh(consultation)
    return consultation

# DELETE data from database
def delete_consultation(db:Session, consultation_id: int):
    db_consultation = get_consultation_by_id(db, consultation_id)
    db.delete(db_consultation)
    db.commit()

