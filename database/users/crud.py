"""This module contains CRUD methods for database User model"""

from pydantic import EmailStr
from sqlalchemy.orm import Session

from database.users import models, schemas
from services import hash_password


# CREATE data in database
def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = hash_password(user.password)
    db_user = models.User(
        email=user.email,
        phone=user.phone,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# READ data from database
def get_user_by_user_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(db: Session, email: EmailStr):
    return db.query(models.User).filter(models.User.email == email).first()

def get_all_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

# UPDATE data in database
def update_user_email(db: Session, user_id: int, email: EmailStr):
    db_user = get_user_by_user_id(db, user_id)
    db_user.email = email
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user_phone(db: Session, user_id: int, phone: str):
    db_user = get_user_by_user_id(db, user_id)
    db_user.phone = phone
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user_password(db: Session, user_id: int, password: str):
    db_user = get_user_by_user_id(db, user_id)
    hashed_password = hash_password(password)
    db_user.hashed_password = hashed_password
    db.commit()
    db.refresh(db_user)
    return db_user

# DELETE data from database
def delete_user(db: Session, user_id: int):
    db_user = get_user_by_user_id(db, user_id)
    db.delete(db_user)
    db.commit()

