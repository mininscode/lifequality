"""This module contains CRUD operations for the Work model"""

from sqlalchemy.orm import Session

from database.works import models, schemas


# CREATE data in database
def create_work(db: Session, work: schemas.Work):
    db_work = models.Work(
        name=work.name,
        is_emergency=work.is_emergency,
        duration=work.duration
    )
    db.add(db_work)
    db.commit()
    db.refresh(db_work)
    return db_work

# READ data from database
def get_work_by_id(db: Session, work_id: int):
    return db.query(models.Work).filter(models.Work.id == work_id).first()

def get_work_by_name(db: Session, work_name: str):
    return db.query(models.Work).filter(models.Work.name == work_name).first()

def get_works_by_emergency_status(db: Session, emergency_status: bool, \
                                  skip: int = 0, limit: int = 100):
    return db.query(models.Work).filter(\
                    models.Work.is_emergency == \
                    emergency_status).offset(skip).limit(limit).all()

def get_works_by_duration(db: Session, duration: int, \
                           skip: int = 0, limit: int = 100):
    return db.query(models.Work).filter(\
                    models.Work.duration == duration).offset(\
                    skip).limit(limit).all()

def get_all_works(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Work).offset(skip).limit(limit).all()

# UPDATE data in database
def update_work_name(db: Session, work: schemas.Work, new_work_name: str):
    work.name = new_work_name
    db.commit()
    db.refresh(work)
    return work

def update_work_emergency_status(db: Session, work: schemas.Work, \
                                 new_emergency_status: bool):
    work.is_emergency = new_emergency_status
    db.commit()
    db.refresh(work)
    return work

def update_work_duration(db: Session, work: schemas.Work, duration: int):
    work.duration = duration
    db.commit()
    db.refresh(work)
    return work

# DELETE data from database
def delete_work(db: Session, work_id: int):
    db_work = get_work_by_id(db, work_id)
    db.delete(db_work)
    db.commit()

