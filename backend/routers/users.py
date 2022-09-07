from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder

from database import SessionLocal, engine
from database.users import models, schemas, crud
from ..dependencies import get_token_header

models.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/users",
    tags=["users"],
    dependencies=[Depends(get_token_header)],
    responses={400: {"description": "Not found"}},
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
async def read_users(db=Depends(get_db), skip: int = 0, limit: int = 100):
    users = crud.get_all_users(db, skip=skip, limit=limit)
    json_compatible_users_data = jsonable_encoder(users)
    return json_compatible_users_data
