from fastapi import APIRouter, Depends, HTTPException, Response, status
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

# DATABASE session connect
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CREATE new user
@router.post("/", response_model=schemas.User, status_code=200)
async def create_user(user: schemas.UserCreate, response: Response, \
                      db=Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email alredy registered")
    response.status_code = status.HTTP_201_CREATED
    return crud.create_user(db, user)

# READ users data
@router.get("/", response_model=list[schemas.User], status_code=200)
async def read_users(db=Depends(get_db), skip: int = 0, limit: int = 100):
    db_users = crud.get_all_users(db, skip=skip, limit=limit)
    json_compatible_users_data = jsonable_encoder(db_users)
    return json_compatible_users_data

@router.get("/{user_id}", response_model=schemas.User, status_code=200)
async def read_user(user_id: int, db=Depends(get_db)):
    db_user = crud.get_user_by_user_id(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    json_compatible_user_data = jsonable_encoder(db_user)
    return json_compatible_user_data

# UPDATE users data
@router.put("/{user_id}", response_model=schemas.User, status_code=200)
async def update_user(user: schemas.UserInDB, response: Response, \
                      db=Depends(get_db)):
    db_user = crud.get_user_by_user_id(db, user_id=user.id)
    if db_user.email != user.email:
        updated_user = crud.update_user_email(db, \
                                              user=db_user, \
                                              email=user.email)
        response.status_code = status.HTTP_201_CREATED
        return updated_user
    if db_user.phone != user.phone:
        updated_user = crud.update_user_phone(db, \
                                              user=db_user, \
                                              phone=user.phone)
        response.status_code = status.HTTP_201_CREATED
        return updated_user
    if db_user.hashed_password != user.hashed_password:
        updated_user = crud.update_user_password(db, \
                                                 user=db_user, \
                                                 password=user.hashed_password)
        response.status_code = status.HTTP_201_CREATED
        return updated_user
    raise HTTPException(status_code=400, detail="User data is up to date")

# DELETE user
@router.delete("/{user_id}", status_code=200)
async def delete_user(user_id: int, db=Depends(get_db)):
    db_user = crud.get_user_by_user_id(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    crud.delete_user(db, user_id)
    return f"User {db_user.email} successfully deleted"
        
