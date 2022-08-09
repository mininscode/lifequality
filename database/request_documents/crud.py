"""This module contains CRUD methods for the RequestDocument model"""

from datetime import datetime
from typing import Literal
from sqlalchemy.orm import Session

from database.work_orders import models, schemas


# CREATE data in database
def create_request_document(db: Session, document: schemas.RequestDocument):
    db_order = models.RequestDocument(
        document_type=document.document_type,
        file_path=document.file_path,
        created_at=document.created_at,
        citizen_request_id=document.citizen_request_id,
        contractor_id=document.contractor_id
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

# READ data from database
def get_request_document_by_id(db: Session, document_id: int):
    return db.query(models.RequestDocument).filter(\
                    models.RequestDocument.id == document_id).first()

def get_request_documents_by_document_type(db: Session, document_type: \
                                           Literal['work_order'] | \
                                           Literal['act_of_done_works'], \
                                           skip: int = 0, limit: int = 100):
    return db.query(models.RequestDocument).filter(\
                    models.RequestDocument.document_type == \
                    document_type).offset(skip).limit(limit).all()

def get_request_documents_by_created_at(db: Session, created_at: datetime, \
                                        skip: int = 0, limit: int = 100):
    return db.query(models.RequestDocument).filter(\
                    models.RequestDocument.created_at == \
                    created_at).offset(skip).limit(limit).all()

def get_request_documents_by_citizen_request_id(db: Session, request_id: int, \
                                                skip: int = 0, \
                                                limit: int = 100):
    return db.query(models.RequestDocument).filter(\
                    models.RequestDocument.citizen_request_id == \
                    request_id).offset(skip).limit(limit).all()

def get_request_documents_by_contractor_id(db: Session, contractor_id: int, \
                                           skip: int = 0, limit: int = 100):
    return db.query(models.RequestDocument).filter(\
                    models.RequestDocument.contractor_id == \
                    contractor_id).offset(skip).limit(limit).all()

# UPDATE data in database
def update_request_document_type(db: Session, document_id: int, \
                                 document_type: Literal['work_order'] | \
                                 Literal['act_of_done_works']):
    db_document = get_request_document_by_id(db, document_id)
    db_document.document_type = document_type
    db.commit()
    db.refresh(db_document)
    return db_document

def update_request_document_file_path(db: Session, document_id: int, \
                                      new_file_path: str):
    db_document = get_request_document_by_id(db, document_id)
    db_document.file_path = new_file_path
    db.commit()
    db.refresh(db_document)
    return db_document

def update_request_document_create_date(db: Session, document_id: int, \
                                        created_at: datetime):
    db_document = get_request_document_by_id(db, document_id)
    db_document.created_at = created_at
    db.commit()
    db.refresh(db_document)
    return db_document

def update_request_document_citizen_request_id(db: Session, document_id: int, \
                                               citizen_request_id: int):
    db_document = get_request_document_by_id(db, document_id)
    db_document.citizen_request_id = citizen_request_id
    db.commit()
    db.refresh(db_document)
    return db_document

def update_request_document_contractor_id(db: Session, document_id: int, \
                                          contractor_id: int):
    db_document = get_request_document_by_id(db, document_id)
    db_document.contractor_id = contractor_id
    db.commit()
    db.refresh(db_document)
    return db_document

# DELETE data from database
def delete_request_document(db: Session, document_id: int):
    db_document = get_request_document_by_id(db, document_id)
    db.delete(db_document)
    db.commit()

