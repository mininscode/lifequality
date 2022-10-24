"""This module contains CRUD operations for the Meeting model"""

from datetime import date
from sqlalchemy.orm import Session

from database.meetings import models, schemas


# CREATE data from database
def create_meeting(db: Session, meeting: schemas.Meeting):
    db_meeting = models.Meeting(
        meeting_date=meeting.meeting_date,
        house_id=meeting.house_id,
        is_legal=meeting.is_legal,
        meeting_record=meeting.meeting_record
    )
    db.add(db_meeting)
    db.commit()
    db.refresh(db_meeting)
    return db_meeting

# READ data from database
def get_meeting_by_id(db: Session, meeting_id: int):
    return db.query(models.Meeting).filter(\
                    models.Meeting.id == meeting_id).first()

def get_meeting_by_meeting_record(db: Session, record: str):
    return db.query(models.Meeting).filter(\
                    models.Meeting.meeting_record == record).first()

def get_meetings_by_house_id(db: Session, house_id: int, skip: int = 0, \
                             limit: int = 100):
    return db.query(models.Meeting).filter(\
                    models.Meeting.house_id == \
                    house_id).offset(skip).limit(limit).all()

def get_meetings_by_legal_status(db: Session, is_legal: bool, skip: int = 0, \
                                 limit: int = 100):
    return db.query(models.Meeting).filter(\
                    models.Meeting.is_legal == \
                    is_legal).offset(skip).limit(limit).all()

def get_meetings_by_meeting_date(db: Session, meeting_date: date, \
                                 skip: int = 0, limit: int = 100):
    return db.query(models.Meeting).filter(\
                    models.Meeting.meeting_date == \
                    meeting_date).offset(skip).limit(limit).all()

def get_all_meetings(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Meeting).offset(skip).limit(limit).all()

# UPDATE data in database
def update_meeting_date(db: Session, meeting: schemas.Meeting, \
                        new_date: date):
    meeting.meeting_date = new_date
    db.commit()
    db.refresh(meeting)
    return meeting

def update_meeting_house_id(db: Session, meeting: schemas.Meeting, \
                            new_house_id: int):
    meeting.house_id = new_house_id
    db.commit()
    db.refresh(meeting)
    return meeting

def update_meeting_legal_status(db: Session, meeting: schemas.Meeting, \
                                is_legal: bool):
    meeting.is_legal = is_legal
    db.commit()
    db.refresh(meeting)
    return meeting

def update_meeting_record(db: Session, meeting: schemas.Meeting, \
                          new_meeting_record: str):
    meeting.meeting_record = new_meeting_record
    db.commit()
    db.refresh(meeting)
    return meeting

# DELETE data from database
def delete_meeting(db: Session, meeting_id: int):
    db_meeting = get_meeting_by_id(db, meeting_id)
    db.delete(db_meeting)
    db.commit()

