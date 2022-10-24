from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.encoders import jsonable_encoder

from database import SessionLocal, engine
from database.house_conditions import models, schemas, crud
from ..dependencies import get_token_header


models.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/house_conditions",
    tags=["house_conditions"],
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

# CREATE new house condition
@router.post("/", response_model=schemas.HouseCondition, status_code=200)
async def crate_house_condition(condition: schemas.HouseCondition, \
                                response: Response, db=Depends(get_db)):
    db_condition = crud.get_condition_by_name(db, condition_name=condition.name)
    if db_condition:
        raise HTTPException(status_code=400, \
                            detail="House condition already registered")
    response.status_code = status.HTTP_201_CREATED
    return crud.create_condition(db, condition)

# READ house condition data
@router.get("/", response_model=list[schemas.HouseCondition], status_code=200)
async def read_house_conditions(db=Depends(get_db), skip: int = 0, \
                                limit: int = 100):
    db_conditions = crud.get_all_conditions(db, skip=skip, limit=limit)
    json_compatible_conditions_data = jsonable_encoder(db_conditions)
    return json_compatible_conditions_data

@router.get("/{condition_name}", response_model=schemas.HouseCondition, \
            status_code=200)
async def read_house_condition_by_name(condition_name: str, \
                                       db=Depends(get_db)):
    db_condition = crud.get_condition_by_name(db, condition_name)
    json_compatible_condition_data = jsonable_encoder(db_condition)
    return json_compatible_condition_data

# UPDATE house condition data
@router.put("/{condition_name}", response_model=schemas.HouseCondition, \
            status_code=200)
async def update_house_condition(condition_name: str, new_name: str, \
                                 response: Response, db=Depends(get_db)):
    db_condition = crud.get_condition_by_name(db, condition_name)
    if db_condition.name != new_name:
        updated_condition = crud.update_condition(db, \
                                                  current_name=\
                                                  db_condition.name, \
                                                  new_name=new_name)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_condition_data = jsonable_encoder(updated_condition)
        return json_compatible_condition_data
    return HTTPException(status_code=400, \
                         detail="House condition is up to date")

# DELETE house condition
@router.delete("/{condition_name}", status_code=200)
async def delete_house_condition(condition_name: str, db=Depends(get_db)):
    db_condition = crud.get_condition_by_name(db, condition_name)
    if db_condition is None:
        raise HTTPException(status_code=400, detail="Hose condition not found")
    crud.delete_condition(db, condition_name)
    return f"House condition {condition_name} successfully deleted"

