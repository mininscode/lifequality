"""This module contains CRUD methods for the RequestStatus model"""

from sqlalchemy.orm import Session

from database.request_statuses import models, schemas


# CREATE data in database
def create_request_status(db: Session, status: schemas.RequestStatus):
    db_status = models.RequestStatus(name=status.name)
    db.add(db_status)
    db.commit()
    db.refresh(db_status)
    return db_status

# READ data from database
def get_request_status_by_id(db: Session, status_id: int):
    return db.query(models.RequestStatus).filter(\
                    models.RequestStatus.id == status_id).first()

def get_request_status_by_name(db: Session, status_name: str):
    return db.query(models.RequestStatus).filter(\
                    models.RequestStatus.name == status_name).first()

def get_all_request_statuses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.RequestStatus).offset(skip).limit(limit).all()

# UPDATE data in database
def update_request_status_name(db: Session, status_id: int, new_name: str):
    db_status = get_request_status_by_id(db, status_id)
    db_status.name = new_name
    db.commit()
    db.refresh(db_status)
    return db_status

# DELETE data from database
def delete_request_status(db: Session, status_id: int):
    db_status = get_request_status_by_id(db, status_id)
    db.delete(db_status)
    db.commit()

