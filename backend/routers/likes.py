from fastapi import APIRouter, Depends, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from datetime import datetime

from database import SessionLocal, engine
from database.likes import models, schemas, crud
from ..dependencies import get_token_header


models.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/likes",
    tags=["likes"],
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

# CREATE new like
@router.post("/", response_model=schemas.Like, status_code=200)
async def create_like(like: schemas.Like, response: Response, \
                      db=Depends(get_db)):
    db_like = crud.get_like_by_id(db, like_id=like.id)
    if db_like:
        raise HTTPException(status_code=400, detail="Like already registered")
    response.status_code = status.HTTP_201_CREATED
    return  crud.create_like(db, like)

# READ like data
@router.get("/", response_model=list[schemas.Like], status_code=200)
async def read_likes(db=Depends(get_db), skip: int = 0, limit: int = 100):
    db_likes = crud.get_all_likes(db, skip=skip, limit=limit)
    json_compatible_likes_data = jsonable_encoder(db_likes)
    return json_compatible_likes_data

@router.get("/{like_id}", response_model=schemas.Like, status_code=200)
async def read_like_by_id(like_id: int, db=Depends(get_db)):
    db_like = crud.get_like_by_id(db, like_id)
    json_compatible_like_data = jsonable_encoder(db_like)
    return json_compatible_like_data

@router.get("/request/{request_id}", response_model=list[schemas.Like], \
            status_code=200)
async def read_likes_by_request_id(request_id: int, db=Depends(get_db), \
                                   skip: int = 0, limit: int = 100):
    db_likes = crud.get_likes_by_citizen_request_id(db, request_id, skip=skip, \
                                                  limit=limit)
    json_compatible_likes_data = jsonable_encoder(db_likes)
    return json_compatible_likes_data

@router.get("/author/{author_id}", response_model=list[schemas.Like], \
            status_code=200)
async def read_likes_by_author_id(author_id: int, db=Depends(get_db), \
                                  skip: int = 0, limit: int = 100):
    db_likes = crud.get_likes_by_author_id(db, author_id, skip=skip, \
                                           limit=limit)
    json_compatible_likes_data = jsonable_encoder(db_likes)
    return json_compatible_likes_data

@router.get("/create_date/{created_at}", response_model=list[schemas.Like], \
            status_code=200)
async def read_likes_by_create_date(created_at: datetime, db=Depends(get_db), \
                                    skip: int = 0, limit: int = 100):
    db_likes = crud.get_likes_by_create_date(db, created_at, skip=skip, \
                                             limit=limit)
    json_compatible_likes_data = jsonable_encoder(db_likes)
    return json_compatible_likes_data

# UPDATE like data
@router.put("/{like_id}", response_model=schemas.Like, status_code=200)
async def update_like(like: schemas.Like, response: Response, \
                      db=Depends(get_db)):
    db_like = crud.get_like_by_id(db, like_id=like.id)

    if db_like.citizen_request_id != like.citizen_request_id:
        updated_like = crud.update_like_request_id(db, like=db_like, \
                                                   request_id=\
                                                   like.citizen_request_id)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_like_data = jsonable_encoder(updated_like)
        return json_compatible_like_data

    if db_like.count < like.count:
        updated_like = crud.update_like_count(db, like=db_like)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_like_data = jsonable_encoder(updated_like)
        return json_compatible_like_data

    if db_like.author_id != like.author_id:
        updated_like = crud.update_like_author_id(db, like=db_like, \
                                                  new_author_id=like.author_id)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_like_data = jsonable_encoder(updated_like)
        return json_compatible_like_data

    if db_like.created_at != like.created_at:
        updated_like = crud.update_like_create_date(db, like=db_like, \
                                                    created_at=like.created_at)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_like_data = jsonable_encoder(updated_like)
        return json_compatible_like_data
    return HTTPException(status_code=400, detail="Like is up to date")

# DELETE like
@router.delete("/{like_id}", status_code=200)
async def delete_like(like_id: int, db=Depends(get_db)):
    db_like = crud.get_like_by_id(db, like_id)
    if db_like is None:
        raise HTTPException(status_code=400, detail="Like not found")
    crud.delete_like(db, like_id)
    return f"Like {like_id} successully deleted"

