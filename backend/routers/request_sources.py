from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.encoders import jsonable_encoder

from database import SessionLocal, engine
from database.request_sources import models, schemas, crud
from ..dependencies import get_token_header


models.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/request_sources",
    tags=["request_sources"],
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

# CREATE new request source
@router.post("/", response_model=schemas.RequestSource, status_code=200)
async def create_request_source(source: schemas.RequestSource, \
                                response: Response, db=Depends(get_db)):
    db_source = crud.get_source_by_name(db, name=source.name)
    if db_source:
        raise HTTPException(status_code=400, \
                            detail="Request source already registered")
    response.status_code = status.HTTP_201_CREATED
    return crud.create_request_source(db, source)

# READ request source data
@router.get("/", response_model=list[schemas.RequestSource], status_code=200)
async def read_request_sources(db=Depends(get_db), skip: int = 0, \
                               limit: int = 100):
    db_sources = crud.get_all_sources(db, skip=skip, limit=limit)
    json_compatible_sources_data = jsonable_encoder(db_sources)
    return json_compatible_sources_data

@router.get("/{source_id}", response_model=schemas.RequestSource, \
            status_code=200)
async def read_request_source_by_id(source_id: int, db=Depends(get_db)):
    db_source = crud.get_source_by_id(db, source_id)
    json_compatible_source_data = jsonable_encoder(db_source)
    return json_compatible_source_data

@router.get("/name/{source_name}", response_model=schemas.RequestSource, \
            status_code=200)
async def read_request_source_by_name(name: str, db=Depends(get_db)):
    db_source = crud.get_source_by_name(db, name)
    json_compatible_source_data = jsonable_encoder(db_source)
    return json_compatible_source_data

# UPDATE request source data
@router.put("/{source_id}", response_model=schemas.RequestSource, \
            status_code=200)
async def update_request_source(source: schemas.RequestSource, \
                                response: Response, \
                                db=Depends(get_db)):
    db_source = crud.get_source_by_id(db, source_id=source.id)
    if db_source.name != source.name:
        updated_source = crud.update_source_name(db, source=db_source, \
                                                 new_name=source.name)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_source_data = jsonable_encoder(updated_source)
        return json_compatible_source_data
    return HTTPException(status_code=400, \
                         detail="Request sourrce is up to date")

# DELETE request source
@router.delete("/{source_name}", status_code=200)
async def delete_request_source(name: str, db=Depends(get_db)):
    db_source = crud.get_source_by_name(db, name=name)
    if db_source is None:
        raise HTTPException(status_code=400, detail="Request source not found")
    crud.delete_source(db, name)
    return f"Request source {name} successfully deleted"

