"""This module contains CRUD methods for the Comment model"""

from datetime import datetime
from sqlalchemy.orm import Session

from database.comments import models, schemas


# CREATE data in database
def create_comment(db: Session, comment: schemas.Comment):
    db_comment = models.Comment(
        text=comment.text,
        author=comment.author,
        created_at=comment.created_at,
        citizen_request_id=comment.citizen_request_id
    )
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

# READ data from database
def get_comment_by_id(db: Session, comment_id: int):
    return db.query(models.Comment).filter(\
                    models.Comment.id == comment_id).first()

def get_comments_by_author(db: Session, author: str, skip: int = 0, \
                           limit: int = 100):
    return db.query(models.Comment).filter(\
                    models.Comment.author == \
                    author).offset(skip).limit(limit).all()

def get_comments_by_created_at(db: Session, created_at: datetime, \
                               skip: int = 0, limit: int = 100):
    return db.query(models.Comment).filter(\
                    models.Comment.created_at == \
                    created_at).offset(skip).limit(limit).all()

def get_comments_by_citizen_request_id(db: Session, request_id: int, \
                                       skip: int = 0, limit: int = 100):
    return db.query(models.Comment).filter(\
                    models.Comment.citizen_request_id == \
                    request_id).offset(skip).limit(limit).all()

def get_all_comments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Comment).offset(skip).limit(limit).all()

# UPDATE data in database
def update_comment_text(db: Session, comment_id: int, new_text: str):
    db_comment = get_comment_by_id(db, comment_id)
    db_comment.text = new_text
    db.commit()
    db.refresh(db_comment)
    return db_comment

def update_comment_author(db: Session, comment_id: int, new_author: str):
    db_comment = get_comment_by_id(db, comment_id)
    db_comment.author = new_author
    db.commit()
    db.refresh(db_comment)
    return db_comment

def update_comment_create_date(db: Session, comment_id: int, \
                               created_at: datetime):
    db_comment = get_comment_by_id(db, comment_id)
    db_comment.created_at = created_at
    db.commit()
    db.refresh(db_comment)
    return db_comment

def update_comment_citizen_request_id(db: Session, comment_id: int, \
                                      citizen_request_id: int):
    db_comment = get_comment_by_id(db, comment_id)
    db_comment.citizen_request_id = citizen_request_id
    db.commit()
    db.refresh(db_comment)
    return db_comment

# DELETE data from database
def delete_comment(db: Session, comment_id: int):
    db_comment = get_comment_by_id(db, comment_id)
    db.delete(db_comment)
    db.commit()

