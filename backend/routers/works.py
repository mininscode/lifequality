from fastapi import APIRouter, Depends, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder

from database import SessionLocal, engine
from database.works import models, schemas, crud
from ..dependencies import get_token_header


models.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/works",
    tags=["works"],
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

# CREATE new work
@router.post("/", response_model=schemas.Work, status_code=200)
async def create_work(work: schemas.Work, response: Response, \
                      db=Depends(get_db)):
    db_work = crud.get_work_by_id(db, work_id=work.id)
    if db_work:
        raise HTTPException(status_code=400, detail="Work already registered")
    response.status_code = status.HTTP_201_CREATED
    return crud.create_work(db, work)

# READ work data
@router.get("/", response_model=list[schemas.Work], status_code=200)
async def read_works(db=Depends(get_db), skip: int = 0, limit: int = 100):
    db_works = crud.get_all_works(db, skip=skip, limit=limit)
    json_compatible_works_data = jsonable_encoder(db_works)
    return json_compatible_works_data

@router.get("/{work_id}", response_model=schemas.Work, status_code=200)
async def read_work_by_id(work_id: int, db=Depends(get_db)):
    db_work = crud.get_work_by_id(db, work_id)
    json_compatible_work_data = jsonable_encoder(db_work)
    return json_compatible_work_data

@router.get("/name/{work_name}", response_model=schemas.Work, status_code=200)
async def read_work_by_name(work_name: str, db=Depends(get_db)):
    db_work = crud.get_work_by_name(db, work_name)
    json_compatible_work_data = jsonable_encoder(db_work)
    return json_compatible_work_data

@router.get("/emergency_status/{emergency_status}", \
            response_model=list[schemas.Work], status_code=200)
async def read_works_by_emergency_status(emergency_status: bool, \
                                         db=Depends(get_db), \
                                         skip: int = 0, \
                                         limit: int = 100):
    db_works = crud.get_works_by_emergency_status(db, emergency_status, \
                                                  skip=skip, limit=limit)
    json_compatible_works_data = jsonable_encoder(db_works)
    return json_compatible_works_data

@router.get("/duration/{duration}", response_model=list[schemas.Work], \
            status_code=200)
async def read_works_by_duration(duration: int, db=Depends(get_db), \
                                 skip: int = 0, limit: int = 100):
    db_works = crud.get_works_by_duration(db, duration, skip=skip, limit=limit)
    json_compatible_works_data = jsonable_encoder(db_works)
    return json_compatible_works_data

# UPDATE work data
@router.put("/{work_id}", response_model=schemas.Work, status_code=200)
async def update_work(work: schemas.Work, response: Response, \
                      db=Depends(get_db)):
    db_work = crud.get_work_by_id(db, work_id=work.id)
    
    if db_work.name != work.name:
        updated_work = crud.update_work_name(db, work=db_work, \
                                             new_work_name=work.name)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_work_data = jsonable_encoder(updated_work)
        return json_compatible_work_data

    if db_work.is_emergency != work.is_emergency:
        updated_work = crud.update_work_emergency_status(db, work=db_work, \
                                                         new_emergency_status=\
                                                         work.is_emergency)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_work_data = jsonable_encoder(updated_work)
        return json_compatible_work_data

    if db_work.duration != work.duration:
        updated_work = crud.update_work_duration(db, work=db_work, \
                                                 duration=work.duration)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_work_data = jsonable_encoder(updated_work)
        return json_compatible_work_data
    return HTTPException(status_code=400, detail="Work is up to date")

# DELETE work
@router.delete("/{work_id}", status_code=200)
async def delete_work(work_id: int, db=Depends(get_db)):
    db_work = crud.get_work_by_id(db, work_id)
    if db_work is None:
        raise HTTPException(status_code=400, detail="Work not found")
    crud.delete_work(db, work_id)
    return f"Work {db_work.name} successfully deleted"

