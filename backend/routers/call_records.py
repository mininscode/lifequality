from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.encoders import jsonable_encoder
from datetime import datetime

from database import SessionLocal, engine
from database.call_records import models, schemas, crud
from ..dependencies import get_token_header

models.Base.metadata.create_all(bind=engine)

router=APIRouter(
    prefix="/call_records",
    tags=["call_records"],
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

# CREATE new call reecord
@router.post("/", response_model=schemas.CallRecord, status_code=200)
async def create_call_record(call_record: schemas.CallRecord, \
                             response: Response, db=Depends(get_db)):
    db_call_record = crud.get_call_record_by_id(db, record_id=call_record.id)
    if db_call_record:
        raise HTTPException(status_code=400, \
                            detail="Call record already registered")
    response.status_code = status.HTTP_201_CREATED
    return crud.create_call_record(db, call_record)

# READ call record data
@router.get("/{record_id}", response_model=schemas.CallRecord, status_code=200)
async def read_call_record_by_id(record_id: int, db=Depends(get_db)):
    db_call_record = crud.get_call_record_by_id(db, record_id)
    json_compatible_call_record_data = jsonable_encoder(db_call_record)
    return json_compatible_call_record_data

@router.get("/created_at/{created_at}", response_model=list[schemas.CallRecord], \
            status_code=200)
async def read_call_records_by_create_date(created_at: datetime, \
                                           db=Depends(get_db), \
                                           skip: int = 0, \
                                           limit: int = 100):
    db_call_records = crud.get_call_records_by_create_date(db, \
                                                           created_at, \
                                                           skip=skip, \
                                                           limit=limit)
    json_compatible_call_records_data = jsonable_encoder(db_call_records)
    return json_compatible_call_records_data

@router.get("/citizen/{citizen_id}", response_model=list[schemas.CallRecord], \
            status_code=200)
async def read_call_records_by_citizen_id(citizen_id: int, db=Depends(get_db), \
                                          skip: int = 0, limit: int = 100):
    db_call_records = crud.get_call_records_by_citizen_id(db, \
                                                          citizen_id, \
                                                          skip=skip, \
                                                          limit=limit)
    json_compatible_call_records_data = jsonable_encoder(db_call_records)
    return json_compatible_call_records_data

@router.get("/employee/{employee_id}", response_model=list[schemas.CallRecord], \
            status_code=200)
async def read_call_records_by_employee_id(employee_id: int, db=Depends(get_db), \
                                           skip: int = 0, limit: int = 100):
    db_call_records = crud.get_call_records_by_employee_id(db, \
                                                           employee_id, \
                                                           skip=skip, \
                                                           limit=limit)
    json_compatible_call_records_data = jsonable_encoder(db_call_records)
    return json_compatible_call_records_data

@router.get("/", response_model=list[schemas.CallRecord], status_code=200)
async def read_all_call_records(db=Depends(get_db), skip: int = 0, \
                                limit: int = 100):
    db_call_records = crud.get_all_call_records(db, skip=skip, limit=limit)
    json_compatible_call_records_data = jsonable_encoder(db_call_records)
    return json_compatible_call_records_data

# UPDATE call record data
@router.put("/{record_id}", response_model=schemas.CallRecord, status_code=200)
async def update_call_record(call_record: schemas.CallRecord, \
                             response: Response, \
                             db=Depends(get_db)):
    db_call_record = crud.get_call_record_by_id(db, record_id=call_record.id)

    if db_call_record.file_path != call_record.file_path:
        updated_call_record = crud.update_call_record_file_path(db, \
                                                                record=db_call_record, \
                                                                file_path=call_record.file_path)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_call_record_data = jsonable_encoder(updated_call_record)
        return json_compatible_call_record_data

    if db_call_record.created_at != call_record.created_at:
        updated_call_record = crud.update_call_record_create_date(db, \
                                                                  record=db_call_record, \
                                                                  created_at=call_record.created_at)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_call_record_data = jsonable_encoder(updated_call_record)
        return json_compatible_call_record_data

    if db_call_record.citizen_id != call_record.citizen_id:
        updated_call_record = crud.update_call_record_citizen_id(db, \
                                                                 record=db_call_record, \
                                                                 citizen_id=call_record.citizen_id)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_call_record_data = jsonable_encoder(updated_call_record)
        return json_compatible_call_record_data

    if db_call_record.emplyee_id != call_record.employee_id:
        updated_call_record = crud.update_call_record_employee_id(db, \
                                                                  record=db_call_record, \
                                                                  employee_id=call_record.employee_id)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_call_record_data = jsonable_encoder(updated_call_record)
        return json_compatible_call_record_data
    return HTTPException(status_code=400, detail="Call record is up to date")

# DELETE call record
@router.delete("/{record_id}", status_code=200)
async def delete_call_record(record_id: int, db=Depends(get_db)):
    db_call_record = crud.get_call_record_by_id(db, record_id)
    if db_call_record is None:
        raise HTTPException(status_code=400, detail="Call record not found")
    crud.delete_call_record(db, record_id)
    return f"Call record {record_id} successfully deleted"

