from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.encoders import jsonable_encoder
from datetime import datetime

from database import SessionLocal, engine
from database.client_requests import models, schemas, crud
from ..dependencies import get_token_header

models.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/client_requests",
    tags=["client_requests"],
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

# CREATE new client request
@router.post("/", response_model=schemas.ClientRequest, status_code=200)
async def create_client_request(request: schemas.ClientRequest, \
                                response: Response, \
                                db=Depends(get_db)):
    db_client_request = crud.get_client_request_by_id(db, request_id=request.id)
    if db_client_request:
        raise HTTPException(status_code=400, \
                            detail="Client request already registered")
    response.status_code = status.HTTP_201_CREATED
    return crud.create_client_request(db, request)

# READ client request data
@router.get("/{request_id}", response_model=schemas.ClientRequest, \
             status_code=200)
async def read_client_request_by_id(request_id: int, db=Depends(get_db)):
    db_client_request = crud.get_client_request_by_id(db, request_id)
    json_compatible_client_request_data = jsonable_encoder(db_client_request)
    return json_compatible_client_request_data

@router.get("/citizen/{citizen_id}", response_model=list[schemas.ClientRequest], \
            status_code=200)
async def read_client_requests_by_citizen_id(citizen_id: int, \
                                             db=Depends(get_db), \
                                             skip: int = 0, \
                                             limit: int = 100):
    db_client_requests = crud.get_client_requests_by_citizen_id(db, \
                                                                citizen_id, \
                                                                skip = skip, \
                                                                limit = limit)
    json_compatible_client_requests_data = jsonable_encoder(db_client_requests)
    return json_compatible_client_requests_data

@router.get("/address/{address}", response_model=list[schemas.ClientRequest], \
            status_code=200)
async def read_client_requests_by_address(address: str, \
                                          db=Depends(get_db), \
                                          skip: int = 0, \
                                          limit: int = 100):
    db_client_requests = crud.get_client_requests_by_address(db, \
                                                             address, \
                                                             skip = skip, \
                                                             limit = limit)
    json_compatible_client_requests_data = jsonable_encoder(db_client_requests)
    return json_compatible_client_requests_data

@router.get("/source/{request_source}", response_model=list[schemas.ClientRequest], \
            status_code=200)
async def read_client_requests_by_source(request_source: int, \
                                         db=Depends(get_db), \
                                         skip: int = 0, \
                                         limit: int = 100):
    db_client_requests = crud.get_client_requests_by_source(db, \
                                                            request_source, \
                                                            skip = skip, \
                                                            limit = limit)
    json_compatible_client_requests_data = jsonable_encoder(db_client_requests)
    return json_compatible_client_requests_data

@router.get("/created/{created_at}", response_model=list[schemas.ClientRequest], \
            status_code=200)
async def read_client_requests_by_create_date(created_at: datetime, \
                                              db=Depends(get_db), \
                                              skip: int = 0, \
                                              limit: int = 100):
    db_client_requests = crud.get_client_requests_by_create_date(db, \
                                                                 created_at, \
                                                                 skip = skip, \
                                                                 limit = limit)
    json_compatible_client_requests_data = jsonable_encoder(db_client_requests)
    return json_compatible_client_requests_data

@router.get("/updated/{updated_at}", response_model=list[schemas.ClientRequest], \
            status_code=200)
async def read_client_requests_by_update_date(updated_at: datetime, \
                                              db=Depends(get_db), \
                                              skip: int = 0, \
                                              limit: int = 100):
    db_client_requests = crud.get_client_requests_by_update_date(db, \
                                                                 updated_at, \
                                                                 skip = skip, \
                                                                 limit = limit)
    json_compatible_client_requests_data = jsonable_encoder(db_client_requests)
    return json_compatible_client_requests_data

@router.get("/closed/{closed_at}", response_model=list[schemas.ClientRequest], \
            status_code=200)
async def read_client_requests_by_close_date(closed_at: datetime, \
                                             db=Depends(get_db), \
                                             skip: int = 0, \
                                             limit: int = 100):
    db_client_requests = crud.get_client_requests_by_close_date(db, \
                                                                closed_at, \
                                                                skip = skip, \
                                                                limit = limit)
    json_compatible_client_requests_data = jsonable_encoder(db_client_requests)
    return json_compatible_client_requests_data

@router.get("/duration/{fact_duration}", response_model=list[schemas.ClientRequest], \
            status_code=200)
async def read_client_requests_by_fact_duration(fact_duration: datetime, \
                                                db=Depends(get_db), \
                                                skip: int = 0, \
                                                limit: int = 100):
    db_client_requests = crud.get_client_requests_by_fact_duration(db, \
                                                                   fact_duration, \
                                                                   skip = skip,
                                                                   limit = limit)
    json_compatible_client_requests_data = jsonable_encoder(db_client_requests)
    return json_compatible_client_requests_data

@router.get("/request_status/{request_status}", response_model=list[schemas.ClientRequest], \
            status_code=200)
async def read_call_requests_by_request_status(request_status: int, \
                                               db=Depends(get_db), \
                                               skip: int = 0, \
                                               limit: int = 100):
    db_client_requests = crud.get_client_requests_by_request_status(db, \
                                                                    request_status, \
                                                                    skip = skip, \
                                                                    limit = limit)
    json_compatible_client_requests_data = jsonable_encoder(db_client_requests)
    return json_compatible_client_requests_data

@router.get("/feedback/{citizen_feedback}", response_model=list[schemas.ClientRequest], \
            status_code=200)
async def read_client_requests_by_citizen_feedback(citizen_feedback: str, \
                                                   db=Depends(get_db), \
                                                   skip: int = 0, \
                                                   limit: int = 100):
    db_client_requests = crud.get_client_requests_by_citizen_feedback(db, \
                                                                      citizen_feedback, \
                                                                      skip = skip, \
                                                                      limit = limit)
    json_compatible_client_requests_data = jsonable_encoder(db_client_requests)
    return json_compatible_client_requests_data

@router.get("/activity_status/{activity_status}", response_model=list[schemas.ClientRequest], \
            status_code=200)
async def read_client_requests_by_activity_status(is_active: bool, \
                                                  db=Depends(get_db), \
                                                  skip: int = 0, \
                                                  limit: int = 100):
    db_client_requests = crud.get_client_requests_by_activity_status(db, \
                                                                     is_active, \
                                                                     skip = skip, \
                                                                     limit = limit)
    json_compatible_client_requests_data = jsonable_encoder(db_client_requests)
    return json_compatible_client_requests_data

@router.get("/", response_model=list[schemas.ClientRequest], status_code=200)
async def read_all_client_requests(db=Depends(get_db), skip: int = 0, \
                                   limit: int = 100):
    db_client_requests = crud.get_all_client_requests(db, skip=skip, limit=limit)
    json_compatible_client_requests_data = jsonable_encoder(db_client_requests)
    return json_compatible_client_requests_data

# UPDATE client request data
@router.put("/{rquest_id}", response_model=schemas.ClientRequest, \
            status_code=200)
async def update_client_request(request: schemas.ClientRequest, \
                                response: Response, \
                                db=Depends(get_db)):
    db_request = crud.get_client_request_by_id(db, request_id=request.id)
    
    if db_request.text != request.id:
        updated_request = crud.update_client_request_text(db, \
                                                          request=db_request, \
                                                          new_text=request.text)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_client_request_data = jsonable_encoder(updated_request)
        return json_compatible_client_request_data

    if db_request.citizen_id != request.citizen_id:
        updated_request = crud.update_client_request_citizen_id(db, \
                                                                request=db_request, \
                                                                citizen_id=request.citizen_id)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_client_request_data = jsonable_encoder(updated_request)
        return json_compatible_client_request_data

    if db_request.address != request.address:
        updated_request = crud.update_client_request_address(db, \
                                                             request=db_request, \
                                                             address=request.address)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_client_request_data = jsonable_encoder(updated_request)
        return json_compatible_client_request_data

    if db_request.request_source != request.request-source:
        updated_request = crud.update_client_request_source(db, \
                                                            request=db_request, \
                                                            source=request.request_source)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_client_request_data = jsonable_encoder(updated_request)
        return json_compatible_client_request_data

    if db_request.created_at != request.created_at:
        updated_request = crud.update_client_request_create_date(db, \
                                                                 request=db_request, \
                                                                 created_at=request.created_at)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_client_request_data = jsonable_encoder(updated_request)
        return json_compatible_client_request_data

    if db_request.updated_at != request.updated_at:
        updated_request = crud.update_client_request_update_date(db, \
                                                                 request=db_request, \
                                                                 updated_at=request.updated_at)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_client_request_data = jsonable_encoder(updated_request)
        return json_compatible_client_request_data

    if db_request.closed_at != request.closed_at:
        updated_request = crud.update_client_request_close_date(db, \
                                                                request=db_request, \
                                                                closed_at=request.closed_at)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_client_request_data = jsonable_encoder(updated_request)
        return json_compatible_client_request_data

    if db_request.fact_duration != request.fact_duration:
        updated_request = crud.update_client_request_fact_duration(db, \
                                                                   request=db_request, \
                                                                   fact_duration=request.fact_duration)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_client_request_data = jsonable_encoder(updated_request)
        return json_compatible_client_request_data

    if db_request.request_status != request.request_status:
        updated_request = crud.update_client_request_status(db, \
                                                            request=db_request, \
                                                            status=request.request_status)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_client_request_data = jsonable_encoder(updated_request)
        return json_compatible_client_request_data

    if db_request.citizen_feedback != request.citizen_feedback:
        updated_request = crud.update_client_request_citizen_feedback(db, \
                                                                      request=db_request, \
                                                                      citizen_feedback=request.citizen_feedback)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_client_request_data = jsonable_encoder(updated_request)
        return json_compatible_client_request_data

    if db_request.is_active != request.is_active:
        updated_request = crud.update_client_request_activity_status(db, \
                                                                     request=db_request, \
                                                                     is_active=request.is_active)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_client_request_data = jsonable_encoder(updated_request)
        return json_compatible_client_request_data
    return HTTPException(status_code=400, detail="Client request is up to date")

# DELETE client request
@router.delete("/{request_id}", status_code=200)
async def delete_client_request(request_id: int, db=Depends(get_db)):
    db_request = crud.get_client_request_by_id(db, request_id)
    if db_request is None:
        raise HTTPException(status_code=400, detail="Client request not found")
    crud.delete_client_request(db, request_id)
    return f"Client request {request_id} successfully deleted"

