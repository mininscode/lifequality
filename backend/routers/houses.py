from fastapi import APIRouter, Depends, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder

from database import SessionLocal, engine
from database.houses import models, schemas, crud
from ..dependencies import get_token_header


models.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/houses",
    tags=["houses"],
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

# CREATE new house
@router.post("/", response_model=schemas.House, status_code=200)
async def create_house(house: schemas.House, response: Response, \
                       db=Depends(get_db)):
    db_house = crud.get_house_by_id(db, house_id=house.id)
    if db_house:
        raise HTTPException(status_code=400, \
                            detail="House is already registered")
    response.status_code = status.HTTP_201_CREATED
    return crud.create_house(db, house)

# READ house data
@router.get("/", response_model=list[schemas.House], status_code=200)
async def read_houses(db=Depends(get_db), skip: int = 0, limit: int = 100):
    db_houses = crud.get_all_houses(db, skip=skip, limit=limit)
    json_compatible_houses_data = jsonable_encoder(db_houses)
    return json_compatible_houses_data

@router.get("/{house_id}", response_model=schemas.House, status_code=200)
async def read_house_by_id(house_id: int, db=Depends(get_db)):
    db_house = crud.get_house_by_id(db, house_id)
    json_compatible_house_data = jsonable_encoder(db_house)
    return json_compatible_house_data

@router.get("/city/{city}", response_model=list[schemas.House], \
            status_code=200)
async def read_houses_by_city(city: str, db=Depends(get_db), skip: int = 0, \
                              limit: int = 100):
    db_houses = crud.get_houses_by_city(db, city, skip=skip, limit=limit)
    json_compatible_houses_data = jsonable_encoder(db_houses)
    return json_compatible_houses_data

@router.get("/district/{district}", response_model=list[schemas.House], \
            status_code=200)
async def read_houses_by_district(district: str, db=Depends(get_db), \
                                  skip: int = 0, limit: int = 100):
    db_houses = crud.get_houses_by_district(db, district, skip=skip, \
                                            limit=limit)
    json_compatible_houses_data = jsonable_encoder(db_houses)
    return json_compatible_houses_data

@router.get("/street/{street}", response_model=list[schemas.House], \
            status_code=200)
async def read_houses_by_street(street: str, db=Depends(get_db), \
                                skip: int = 0, limit: int = 100):
    db_houses = crud.get_houses_by_street(db, street, skip=skip, limit=limit)
    json_compatible_houses_data = jsonable_encoder(db_houses)
    return json_compatible_houses_data

@router.get("/house_number/{house_number}", \
            response_model=list[schemas.House], status_code=200)
async def read_houses_by_number(house_number: str, db=Depends(get_db), \
                                skip: int = 0, limit: int =100):
    db_houses = crud.get_houses_by_house_number(db, house_number, skip=skip, \
                                                limit=limit)
    json_compatible_houses_data = jsonable_encoder(db_houses)
    return json_compatible_houses_data

@router.get("/house_condition/{condition}", \
            response_model=list[schemas.House], status_code=200)
async def read_houses_by_house_condition_id(condition_id: int, \
                                            db=Depends(get_db), \
                                            skip: int = 0, limit: int = 100):
    db_houses = crud.get_houses_by_condition_id(db, condition_id, skip=skip, \
                                                limit=limit)
    json_compatible_houses_data = jsonable_encoder(db_houses)
    return json_compatible_houses_data

# UPDATE house data
@router.put("/{house_id}", response_model=schemas.House, status_code=200)
async def update_house(house: schemas.House, response: Response, \
                       db=Depends(get_db)):
    db_house = crud.get_house_by_id(db, house_id=house.id)
    
    if db_house.city != house.city:
        updated_house = crud.update_house_city(db, house=db_house, \
                                               city=house.city)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_house_data = jsonable_encoder(updated_house)
        return json_compatible_house_data

    if db_house.district != house.district:
        updated_house = crud.update_house_district(db, house=db_house, \
                                                   district=house.district)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_house_data = jsonable_encoder(updated_house)
        return json_compatible_house_data

    if db_house.street != house.street:
        updated_house = crud.update_house_street(db, house=db_house, \
                                                 street=house.street)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_house_data = jsonable_encoder(updated_house)
        return json_compatible_house_data

    if db_house.house_number != house.house_number:
        updated_house = crud.update_house_house_number(db, house=db_house, \
                                                       house_number=\
                                                       house.house_number)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_house_data = jsonable_encoder(updated_house)
        return json_compatible_house_data

    if db_house.condition_id != house.condition_id:
        updated_house = crud.update_house_condition_id(db, house=db_house, \
                                                       condition_id=\
                                                       house.condition_id)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_house_data = jsonable_encoder(updated_house)
        return json_compatible_house_data
    return HTTPException(status_code=400, detail="House is up to date")

# DELETE house
@router.delete("/{house_id}", status_code=200)
async def delete_house(house_id: int, db=Depends(get_db)):
    db_house = crud.get_house_by_id(db, house_id)
    if db_house is None:
        raise HTTPException(status_code=400, detail="House not found")
    crud.delete_house(db, house_id)
    return f"House {house_id} successfully deleted"

