"""This module contains CRUD methods for the WorkOrder model"""

from datetime import datetime
from sqlalchemy.orm import Session

from database.work_orders import models, schemas


# CREATE data in database
def create_work_order(db: Session, work_order: schemas.WorkOrder):
    db_order = models.WorkOrder(
        file_path=work_order.file_path,
        created_at=work_order.created_at,
        citizen_request_id=work_order.citizen_request_id,
        contractor_id=work_order.contractor_id
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

# READ data from database
def get_work_order_by_id(db: Session, order_id: int):
    return db.query(models.WorkOrder).filter(\
                    models.WorkOrder.id == order_id).first()

def get_work_orders_by_created_at(db: Session, created_at: datetime, \
                                  skip: int = 0, limit: int = 100):
    return db.query(models.WorkOrder).filter(\
                    models.WorkOrder.created_at == \
                    created_at).offset(skip).limit(limit).all()

def get_work_orders_by_citizen_requestt_id(db: Session, request_id: int, \
                                          skip: int = 0, limit: int = 100):
    return db.query(models.WorkOrder).filter(\
                    models.WorkOrder.citizen_request_id == \
                    request_id).offset(skip).limit(limit).all()

def get_work_orders_by_contractor_id(db: Session, contractor_id: int, \
                                     skip: int = 0, limit: int = 100):
    return db.query(models.WorkOrder).filter(\
                    models.WorkOrder.contractor_id == \
                    contractor_id).offset(skip).limit(limit).all()

# UPDATE data in database
def update_work_order_file_path(db: Session, order_id: int, \
                                new_file_path: str):
    db_order = get_work_order_by_id(db, order_id)
    db_order.file_path = new_file_path
    db.commit()
    db.refresh(db_order)
    return db_order

def update_work_order_create_date(db: Session, order_id: int, \
                                  created_at: datetime):
    db_order = get_work_order_by_id(db, order_id)
    db_order.created_at = created_at
    db.commit()
    db.refresh(db_order)
    return db_order

def update_work_order_citizen_request_id(db: Session, order_id: int, \
                                          citizen_request_id: int):
    db_order = get_work_order_by_id(db, order_id)
    db_order.citizen_request_id = citizen_request_id
    db.commit()
    db.refresh(db_order)
    return db_order

def update_work_order_contractor_id(db: Session, order_id: int, \
                                    contractor_id: int):
    db_order = get_work_order_by_id(db, order_id)
    db_order.contractor_id = contractor_id
    db.commit()
    db.refresh(db_order)
    return db_order

# DELETE data from database
def delete_work_order(db: Session, order_id: int):
    db_order = get_work_order_by_id(db, order_id)
    db.delete(db_order)
    db.commit()

