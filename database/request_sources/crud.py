"""This module contains CRUD operations for the RequestStatuse model"""

from sqlalchemy.orm import Session

from database.request_sources import models, schemas


# CREATE data in database
def create_request_source(db: Session, source: schemas.RequestSource):
    db_source = models.RequestSource(
        name=source.name
    )
    db.add(db_source)
    db.commit()
    db.refresh(db_source)

# READ data from database
def get_source_by_name(db: Session, name: str):
    return db.query(models.RequestSource).filter(\
                    models.RequestSource.name == name).first()

def get_all_sources(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.RequestSource).offset(skip).limit(limit).all()

# UPDATE data in database
def update_source_name(db: Session, name_current: str, name_new: str):
    db_source = get_source_by_name(db, name_current)
    db_source.name = name_new
    db.commit()
    db.refresh(db_source)
    return db_source

#DELETE data from database
def delete_source(db: Session, name: str):
    db_source = get_source_by_name(db, name)
    db.delete(db_source)
    db.commit()

