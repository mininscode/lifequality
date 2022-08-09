"""This module contains CRUD methods for the ClientRequest model"""

from datetime import datetime
from sqlalchemy.orm import Session

from database.client_requests import models, schemas
from validation_types import AddressType


# CREATE data in database
def create_client_request(db: Session, request: schemas.ClientRequest):
    db_request = models.ClientRequest(
        text=request.text,
        citizen_id=request.citizen_id,
        address=request.address,
        request_source=request.request_source,
        created_at=request.created_at,
        updated_at=request.updated_at,
        closed_at=request.closed_at,
        planed_duration=request.planed_duration,
        fact_duration=request.fact_duration,
        request_status=request.request_status,
        citizen_feedback=request.citizen_feedback,
        is_active=request.is_active,
        record_id=request.record_id
    )
    db.add(db_request)
    db.commit()
    db.refresh(db_request)
    return db_request

# READ data from database
def get_client_request_by_id(db: Session, request_id: int):
    return db.query(models.ClientRequest).filter(\
                    models.ClientRequest.id == request_id).first()

def get_client_requests_by_citizen_id(db: Session, citizen_id: int, \
                                      skip: int = 0, limit: int = 100):
    return db.query(models.ClientRequest).filter(\
                    models.ClientRequest.citizen_id == citizen_id).offset(\
                    skip).limit(limit).all()

def get_client_requests_by_address(db: Session, address: AddressType, \
                                   skip: int = 0, limit: int = 100):
    return db.query(models.ClientRequest).filter(\
                    models.ClientRequest.address == address).offset(\
                    skip).limit(limit).all()

def get_client_requests_by_source(db: Session, request_source: str, \
                                  skip: int = 0, limit: int = 100):
    return db.query(models.ClientRequest).filter(\
                    models.ClientRequest.request_source == \
                    request_source).offset(skip).limit(limit).all()

def get_client_requests_by_create_date(db: Session, \
                                       created_at: datetime, \
                                       skip: int = 0, limit: int = 100):
    return db.query(models.ClientRequest).filter(\
                    models.ClientRequest.created_at == \
                    created_at).offset(skip).limit(limit).all()

def get_client_requests_by_update_date(db: Session, updated_at: datetime, \
                                      skip: int = 0, limit: int = 100):
    return db.query(models.ClientRequest).filter(\
                    models.ClientRequest.updated_at == \
                    updated_at).offset(skip).limit(limit).all()

def get_client_requests_by_close_date(db: Session, closed_at: datetime, \
                                      skip: int = 0, limit: int = 100):
    return db.query(models.ClientRequest).filter(\
                    models.ClientRequest.closed_at == \
                    closed_at).offset(skip).limit(limit).all()

def get_client_requests_by_planed_duration(db: Session, \
                                           planed_duration: datetime, \
                                           skip: int = 0, limit: int = 100):
    return db.query(models.ClientRequest).filter(\
                    models.ClientRequest.planed_duration == \
                    planed_duration).offset(skip).limit(limit).all()

def get_client_requests_by_fact_duration(db: Session, \
                                         fact_duration: datetime, \
                                         skip: int = 0, limit: int = 100):
    return db.query(models.ClientRequest).filter(\
                    models.ClientRequest.fact_duration == \
                    fact_duration).offset(skip).limit(limit).all()

def get_client_requests_by_request_status(db: Session, request_status: str, \
                                          skip: int = 0, limit: int = 100):
    return db.query(models.ClientRequest).filter(\
                    models.ClientRequest.request_status == \
                    request_status).offset(skip).limit(limit).all()

def get_client_requests_by_citizen_feedback(db: Session, \
                                            citizen_feedback: str, \
                                            skip: int = 0, limit: int = 100):
    return db.query(models.ClientRequest).filter(\
                    models.ClientRequest.citizen_feedback == \
                    citizen_feedback).offset(skip).limit(limit).all()

def get_client_requests_by_activity_status(db: Session, is_active: bool, \
                                           skip: int = 0, limit: int = 100):
    return db.query(models.ClientRequest).filter(\
                    models.ClientRequest.is_active == \
                    is_active).offset(skip).limit(limit).all()

def get_all_client_requests(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ClientRequest).offset(skip).limit(limit).all()

# UPDATE data in database
def update_client_request_text(db: Session, request_id: int, new_text: str):
    db_request = get_client_request_by_id(db, request_id)
    db_request.text = new_text
    db.commit()
    db.refresh(db_request)
    return db_request

def update_client_request_citizen_id(db: Session, request_id: int, \
                                     citizen_id: int):
    db_request = get_client_request_by_id(db, request_id)
    db_request.citizen_id = citizen_id
    db.commit()
    db.refresh(db_request)
    return db_request

def update_client_request_address(db: Session, request_id: int, \
                                  address: AddressType):
    db_request = get_client_request_by_id(db, request_id)
    db_request.address = address
    db.commit()
    db.refresh(db_request)
    return db_request

def update_client_request_source(db: Session, request_id: int, source: str):
    db_request = get_client_request_by_id(db, request_id)
    db_request.request_source = source
    db.commit()
    db.refresh(db_request)
    return db_request

def update_client_request_create_date(db: Session, request_id: int, \
                                      created_at: datetime):
    db_request = get_client_request_by_id(db, request_id)
    db_request.created_at = created_at
    db.commit()
    db.refresh(db_request)
    return db_request

def update_client_request_update_date(db: Session, request_id: int, \
                                      updated_at: datetime):
    db_request = get_client_request_by_id(db, request_id)
    db_request.updated_at = updated_at
    db.commit()
    db.refresh(db_request)
    return db_request

def update_client_request_close_date(db: Session, request_id: int, \
                                     closed_at: datetime):
    db_request = get_client_request_by_id(db, request_id)
    db_request.closed_at = closed_at
    db.commit()
    db.refresh(db_request)
    return db_request
def update_client_request_planed_duration(db: Session, request_id: int, \
                                          planed_duration: datetime):
    db_request = get_client_request_by_id(db, request_id)
    db_request.planed_duration = planed_duration
    db.commit()
    db.refresh(db_request)
    return db_request

def update_client_request_fact_duration(db: Session, request_id: int, \
                                        fact_duration: datetime):
    db_request = get_client_request_by_id(db, request_id)
    db_request.fact_duration = fact_duration
    db.commit()
    db.refresh(db_request)
    return db_request

def update_client_request_status(db: Session, request_id: int, status: str):
    db_request = get_client_request_by_id(db, request_id)
    db_request.request_status = status
    db.commit()
    db.refresh(db_request)
    return db_request

def update_client_request_citizen_feedback(db: Session, request_id: int, \
                                           citizen_feedback: str):
    db_request = get_client_request_by_id(db, request_id)
    db_request.citizen_feedback = citizen_feedback
    db.commit()
    db.refresh(db_request)
    return db_request

def update_client_request_activity_status(db: Session, request_id: int, \
                                          is_active: bool):
    db_request = get_client_request_by_id(db, request_id)
    db_request.is_active = is_active
    db.commit()
    db.refresh(db_request)
    return db_request

def update_client_request_call_record(db: Session, request_id: int, \
                                      record_id: int):
    db_request = get_client_request_by_id(db, request_id)
    db_request.record_id = record_id
    db.commit()
    db.refresh(db_request)
    return db_request

# DELETE data from database
def delete_client_request(db: Session, request_id: int):
    db_request = get_client_request_by_id(db, request_id)
    db.delete(db_request)
    db.commit()

