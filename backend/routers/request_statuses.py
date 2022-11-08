from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.encoders import jsonable_encoder

from database import SessionLocal, engine
from database.request_statuses import models, schemas, crud
from ..dependencies import get_token_header


models.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/request_statuses",
    tags=["request_statuses"],
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

# CREATE new request status
@router.post("/", response_model=schemas.RequestStatus, status_code=200)
async def create_request_status(request_status: schemas.RequestStatus, \
                                response: Response, db=Depends(get_db)):
    db_status = crud.get_request_status_by_id(db, status_id=request_status.id)
    if db_status:
        raise HTTPException(status_code=400, \
                            detail="Request status already registered")
    response.status_code = status.HTTP_201_CREATED
    return crud.create_request_status(db, status=request_status)

# READ request status data
@router.get("/", response_model=list[schemas.RequestStatus], status_code=200)
async def read_request_statuses(db=Depends(get_db), skip: int = 0, \
                                limit: int = 100):
    db_statuses = crud.get_all_request_statuses(db, skip=skip, limit=limit)
    json_compatible_statuses_data = jsonable_encoder(db_statuses)
    return json_compatible_statuses_data

@router.get("/{status_id}", response_model=schemas.RequestStatus, \
            status_code=200)
async def read_request_status_by_id(status_id: int, db=Depends(get_db)):
    db_status = crud.get_request_status_by_id(db, status_id)
    json_compatible_statuse_data = jsonable_encoder(db_status)
    return json_compatible_statuse_data

@router.get("/name/{status_name}", response_model=schemas.RequestStatus, \
            status_code=200)
async def read_request_status_by_name(status_name: str, db=Depends(get_db)):
    db_status = crud.get_request_status_by_name(db, status_name)
    json_compatible_statuse_data = jsonable_encoder(db_status)
    return json_compatible_statuse_data

# UPDATE request status data
@router.put("/{status_id}", response_model=schemas.RequestStatus, \
            status_code=200)
async def update_request_status(request_status: schemas.RequestStatus, \
                                response: Response, db=Depends(get_db)):
    db_status = crud.get_request_status_by_id(db, status_id=request_status.id)
    if db_status.name != request_status.name:
        updated_status = crud.update_request_status_name(db, \
                                                         status=db_status, \
                                                         new_name=\
                                                         request_status.name)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_statuse_data = jsonable_encoder(updated_status)
        return json_compatible_statuse_data
    return HTTPException(status_code=400, \
                         detail="Request status is up to date")

# DELETE request status
@router.delete("/{status_id}", status_code=200)
async def delete_request_status(status_id: int, db=Depends(get_db)):
    db_status = crud.get_request_status_by_id(db, status_id)
    if db_status is None:
        raise HTTPException(status_code=400, \
                            detail="Request status not found")
    crud.delete_request_status(db, status_id)
    return f"Request status {db_status.name} successfully deleted"

