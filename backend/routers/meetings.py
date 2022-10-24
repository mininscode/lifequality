from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.encoders import jsonable_encoder
from datetime import date

from database import SessionLocal, engine
from database.meetings import models, schemas,crud
from ..dependencies import get_token_header


models.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/meetings",
    tags=["meetings"],
    dependencies=[Depends(get_token_header)],
    responses={400: {"description": "Not found"}},
)

# DATABASE session connect
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CREATE new meeting
@router.post("/", response_model=schemas.Meeting, status_code=200)
async def create_meeting(meeting: schemas.Meeting, response: Response, \
                         db=Depends(get_db)):
    db_meeting = crud.get_meeting_by_id(db, meeting_id=meeting.id)
    if db_meeting:
        raise HTTPException(status_code=400, \
                            detail="Meeting already registered")
    response.status_code = status.HTTP_201_CREATED
    return crud.create_meeting(db, meeting)

# READ meeting data
@router.get("/", response_model=list[schemas.Meeting], status_code=200)
async def read_meetings(db=Depends(get_db), skip: int = 0, limit: int = 100):
    db_meetings = crud.get_all_meetings(db, skip=skip, limit=limit)
    json_compatible_meetings_data = jsonable_encoder(db_meetings)
    return json_compatible_meetings_data

@router.get("/{meeting_id}", response_model=schemas.Meeting, status_code=200)
async def read_meeting_by_id(meeting_id: int, db=Depends(get_db)):
    db_meeting = crud.get_meeting_by_id(db, meeting_id)
    json_compatible_meeting_data = jsonable_encoder(db_meeting)
    return json_compatible_meeting_data

@router.get("/house/{house_id}", response_model=list[schemas.Meeting], \
            status_code=200)
async def read_meetings_by_house_id(house_id: int, db=Depends(get_db), \
                                    skip: int = 0, limit: int = 100):
    db_meetings = crud.get_meetings_by_house_id(db, house_id, skip=skip, \
                                                limit=limit)
    json_compatible_meetings_data = jsonable_encoder(db_meetings)
    return json_compatible_meetings_data

@router.get("/legal_status/{is_legal}", response_model=list[schemas.Meeting], \
            status_code=200)
async def read_meetings_by_legal_status(is_legal: bool, db=Depends(get_db), \
                                        skip: int = 0, limit: int = 100):
    db_meetings = crud.get_meetings_by_legal_status(db, is_legal, skip=skip, \
                                                    limit=limit)
    json_compatible_meetings_data = jsonable_encoder(db_meetings)
    return json_compatible_meetings_data

@router.get("/meeting_date/{meeting_date}", \
            response_model=list[schemas.Meeting], status_code=200)
async def read_meetings_by_meeting_date(meeting_date: date, \
                                        db=Depends(get_db), skip: int = 0, \
                                        limit: int = 100):
    db_meetings = crud.get_meetings_by_meeting_date(db, meeting_date, \
                                                    skip=skip, limit=limit)
    json_compatible_meetings_data = jsonable_encoder(db_meetings)
    return json_compatible_meetings_data

@router.get("/record/{meeting_record}", response_model=schemas.Meeting, \
            status_code=200)
async def read_meeting_by_meeting_record(meeting_record: str, \
                                        db=Depends(get_db)):
    db_meeting = crud.get_meeting_by_meeting_record(db, meeting_record)
    json_compatible_meeting_data = jsonable_encoder(db_meeting)
    return json_compatible_meeting_data

# UPDATE meeting data
@router.put("/{meeting_id}", response_model=schemas.Meeting, status_code=200)
async def update_meeting(meeting: schemas.Meeting, response: Response, \
                         db=Depends(get_db)):
    db_meeting = crud.get_meeting_by_id(db, meeting_id=meeting.id)

    if db_meeting.meeting_date != meeting.meeting_date:
        updated_meeting = crud.update_meeting_date(db, \
                                                   meeting=db_meeting, \
                                                   new_date=\
                                                   meeting.meeting_date)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_meeting_data = jsonable_encoder(updated_meeting)
        return json_compatible_meeting_data

    if db_meeting.house_id != meeting.house_id:
        updated_meeting = crud.update_meeting_house_id(db, \
                                                       meeting=db_meeting, \
                                                       new_house_id=\
                                                       meeting.house_id)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_meeting_data = jsonable_encoder(updated_meeting)
        return json_compatible_meeting_data

    if db_meeting.is_legal != meeting.is_legal:
        updated_meeting = crud.update_meeting_legal_status(db, \
                                                           meeting=db_meeting, \
                                                           is_legal=\
                                                           meeting.is_legal)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_meeting_data = jsonable_encoder(updated_meeting)
        return json_compatible_meeting_data

    if db_meeting.meeting_record != meeting.meeting_record:
        updated_meeting = crud.update_meeting_record(db, meeting=db_meeting, \
                                                     new_meeting_record=\
                                                     meeting.meeting_record)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_meeting_data = jsonable_encoder(updated_meeting)
        return json_compatible_meeting_data
    return HTTPException(status_code=400, detail="Meeting is up to date")

# DELETE meeting
@router.delete("/{meeting_id}", status_code=200)
async def delete_meeting(meeting_id: int, db=Depends(get_db)):
    db_meeting = crud.get_meeting_by_id(db, meeting_id)
    if db_meeting is None:
        raise HTTPException(status_code=400, detail="Meeting not found")
    crud.delete_meeting(db, meeting_id)
    return f"Meeting {meeting_id} successfully deleted"

