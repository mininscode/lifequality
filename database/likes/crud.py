"""This module contains CRUD methods for the Like model"""

from datetime import datetime
from sqlalchemy.orm import Session

from database.likes import models, schemas


# CREATE data in database
def create_like(db: Session, like: schemas.Like):
    db_like = models.Like(
        citizen_request_id=like.citizen_request_id,
        count=like.count,
        author=like.author,
        created_at=like.created_at
    )
    db.add(db_like)
    db.commit()
    db.refresh(db_like)
    return db_like

# READ data from database
def get_like_by_id(db: Session, like_id: int):
    return db.query(models.Like).filter(\
                    models.Like.id == like_id).first()

def get_like_by_citizen_request_id(db: Session, request_id: int):
    return db.query(models.Like).filter(\
                    models.Like.citizen_request_id == request_id).first()

def get_like_by_author(db: Session, author: str):
    return db.query(models.Like).filter(\
                    models.Like.author == author).first()

def get_likes_by_create_date(db: Session, created_at: datetime, \
                             skip: int = 0, limit: int = 100):
    return db.query(models.Like).filter(\
                    models.Like.created_at == \
                    created_at).offset(skip).limit(limit).all()

def gett_all_likes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Like).offset(skip).limit(limit).all()

# UPDATE data in database
def update_like_citizen_request_id(db: Session, like_id: int, request_id: int):
    db_like = get_like_by_id(db, like_id)
    db_like.citizen_request_id = request_id
    db.commit()
    db.refresh(db_like)
    return db_like

def update_like_count(db: Session, like_id: int):
    db_like = get_like_by_id(db, like_id)
    db_like.count += 1
    db.commit()
    db.refresh(db_like)
    return db_like

def update_like_author(db: Session, like_id: int, new_author: str):
    db_like = get_like_by_id(db, like_id)
    db_like.author = new_author
    db.commit()
    db.refresh(db_like)
    return db_like

def update_like_create_date(db: Session, like_id: int, created_at: datetime):
    db_like = get_like_by_id(db, like_id)
    db_like.created_at = created_at
    db.commit()
    db.refresh(db_like)
    return db_like

# DELETE data from database
def delete_like(db: Session, like_id: int):
    db_like = get_like_by_id(db, like_id)
    db.delete(db_like)
    db.commit()

