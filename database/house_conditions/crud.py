"""This module contains CRUD methods for Condition model"""

from sqlalchemy.orm import Session

from database.house_conditions import models, schemas


# CREATE data in database
def create_condition(db: Session, condition: schemas.HouseCondition):
    db_condition = models.HouseCondition(
        name=condition.name
    )
    db.add(db_condition)
    db.commit()
    db.refresh(db_condition)
    return db_condition

# READ data from database
def get_condition_by_name(db: Session, condition_name: str):
    db_condition = db.query(models.HouseCondition).filter(models.HouseCondition.name == \
                   condition_name).first()
    return db_condition

def get_all_conditions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.HouseCondition).offset(skip).limit(limit).all()

# UPDATE data in database
def update_condition(db: Session, current_name: str, new_name: str):
    db_condition = get_condition_by_name(db, current_name)
    db_condition.name = new_name
    db.commit()
    db.refresh(db_condition)
    return db_condition

# DELETE data from database
def delete_condition(db: Session, condition_name: str):
    db_condition = get_condition_by_name(db, condition_name)
    db.delete(db_condition)
    db.commit()

