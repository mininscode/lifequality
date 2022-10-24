"""This module contains CRUD methods for the Like model"""

from datetime import datetime
from sqlalchemy.orm import Session

from database.likes import models, schemas


# CREATE data in database
def create_like(db: Session, like: schemas.Like):
    db_like = models.Like(
        citizen_request_id=like.citizen_request_id,
        count=like.count,
        author_id=like.author_id,
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

def get_likes_by_citizen_request_id(db: Session, request_id: int, \
                                    skip: int = 0, limit: int = 100):
    return db.query(models.Like).filter(\
                    models.Like.citizen_request_id == \
                    request_id).offset(skip).limit(limit).all()

def get_likes_by_author_id(db: Session, author_id: int, skip: int = 0, \
                           limit: int = 100):
    return db.query(models.Like).filter(\
                    models.Like.author_id == \
                    author_id).offset(skip).limit(limit).all()

def get_likes_by_create_date(db: Session, created_at: datetime, \
                             skip: int = 0, limit: int = 100):
    return db.query(models.Like).filter(\
                    models.Like.created_at == \
                    created_at).offset(skip).limit(limit).all()

def get_all_likes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Like).offset(skip).limit(limit).all()

# UPDATE data in database
def update_like_request_id(db: Session, like: schemas.Like, \
                                   request_id: int):
    like.citizen_request_id = request_id
    db.commit()
    db.refresh(like)
    return like

def update_like_count(db: Session, like: schemas.Like):
    like.count += 1
    db.commit()
    db.refresh(like)
    return like

def update_like_author_id(db: Session, like: schemas.Like, new_author_id: int):
    like.author_id = new_author_id
    db.commit()
    db.refresh(like)
    return like

def update_like_create_date(db: Session, like: schemas.Like, \
                            created_at: datetime):
    like.created_at = created_at
    db.commit()
    db.refresh(like)
    return like

# DELETE data from database
def delete_like(db: Session, like_id: int):
    db_like = get_like_by_id(db, like_id)
    db.delete(db_like)
    db.commit()

