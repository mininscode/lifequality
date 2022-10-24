from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.encoders import jsonable_encoder

from database import SessionLocal, engine
from database.clients import models, schemas, crud
from ..dependencies import get_token_header

models.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/clients",
    tags=["clients"],
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

# CREATE new client
@router.post("/", response_model=schemas.Client, status_code=200)
async def create_citizen(citizen: schemas.Client, \
                         response: Response, db=Depends(get_db)):
    db_citizen = crud.get_citizen_by_user_id(db, user_id=citizen.user_id)
    if db_citizen:
        raise HTTPException(status_code=400, detail="Citizen already registered")
    response.status_code = status.HTTP_201_CREATED
    return crud.create_citizen(db, citizen)

# CREATE new client passport
@router.post("/passport/", response_model=schemas.ClientPassport, status_code=200)
async def create_citizen_passport(passport: schemas.ClientPassport, \
                                  response: Response, db=Depends(get_db)):
    db_passport = crud.get_citizen_passport_by_citizen_id(db, \
                                                          citizen_id=passport.citizen_id)
    if db_passport:
        raise HTTPException(status_code=400, detail="Client passport already registered")
    response.status_code = status.HTTP_201_CREATED
    return crud.create_citizen_passport(db, passport)

# READ clients data
@router.get("/", response_model=list[schemas.Client], status_code=200)
async def read_citizens(db=Depends(get_db), skip: int = 0, limit: int = 100):
    db_citizens = crud.get_all_citizens(db, skip=skip, limit=limit)
    json_compatible_citizens_data = jsonable_encoder(db_citizens)
    return json_compatible_citizens_data

@router.get("/{citizen_id}", response_model=schemas.Client, status_code=200)
async def read_citizen(citizen_id: int, db=Depends(get_db)):
    db_citizen = crud.get_citizen_by_citizen_id(db, citizen_id)
    json_compatible_citizen_data = jsonable_encoder(db_citizen)
    return json_compatible_citizen_data

# READ clients passport data
@router.get("/passports/", \
            response_model=list[schemas.ClientPassport], \
            status_code=200)
async def read_all_citizens_passports(db=Depends(get_db), skip: int = 0, \
                                      limit: int = 100):
    db_citizens_passports = crud.get_all_citizens_passports(db, skip=skip, \
                                                           limit=limit)
    json_compatible_all_citizens_passports_data = jsonable_encoder(db_citizens_passports)
    return json_compatible_all_citizens_passports_data

@router.get("/{citizen_id}/passport/", \
            response_model=schemas.ClientPassport, \
            status_code=200)
async def read_citizen_passport(citizen_id: int, db=Depends(get_db)):
    db_citizen_passport = crud.get_citizen_passport_by_citizen_id(db, \
                                                                  citizen_id)
    json_compatible_citizen_passport_data = jsonable_encoder(db_citizen_passport)
    return json_compatible_citizen_passport_data

@router.get("/{citizen_id}/passports", \
            response_model=list[schemas.ClientPassport], status_code=200)
async def read_citizen_all_passports(citizen_id: int, db=Depends(get_db), \
                                     skip: int = 0, limit: int = 100):
    db_citizen_all_passports = crud.get_citizen_all_passports(db, citizen_id, \
                                                              skip=skip, \
                                                              limit=limit)
    json_compatible_citizen_all_passports_data = jsonable_encoder(db_citizen_all_passports)
    return json_compatible_citizen_all_passports_data

# UPDATE clients data
@router.put("/{citizen_id}", response_model=schemas.Client, status_code=200)
async def update_citizen(citizen: schemas.Client, response: Response, \
                         db=Depends(get_db)):
    db_citizen = crud.get_citizen_by_citizen_id(db, citizen_id=citizen.id)
    
    if db_citizen.name != citizen.name:
        updated_citizen = crud.update_citizen_name(db, citizen=db_citizen, \
                                                   name=citizen.name)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_citizen_data = jsonable_encoder(updated_citizen)
        return json_compatible_citizen_data

    if db_citizen.surname != citizen.surname:
        updated_citizen = crud.update_citizen_surname(db, citizen=db_citizen, \
                                                      surname=citizen.surname)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_citizen_data = jsonable_encoder(updated_citizen)
        return json_compatible_citizen_data

    if db_citizen.patronymic != citizen.patronymic:
        updated_citizen = crud.update_citizen_patronymic(db, citizen=db_citizen, \
                                                         patronymic=citizen.patronymic)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_citizen_data = jsonable_encoder(updated_citizen)
        return json_compatible_citizen_data

    if db_citizen.house_id != citizen.house_id:
        updated_citizen = crud.update_citizen_house_id(db, citizen=db_citizen, \
                                                       house_id=citizen.house_id)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_citizen_data = jsonable_encoder(updated_citizen)
        return json_compatible_citizen_data

    if db_citizen.flat_number != citizen.flat_number:
        updated_citizen = crud.update_citizen_flat_number(db, citizen=db_citizen, \
                                                          flat_number=citizen.flat_number)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_citizen_data = jsonable_encoder(updated_citizen)
        return json_compatible_citizen_data

    if db_citizen.is_registered != citizen.is_registered:
        updated_citizen = crud.update_citizen_is_registered(db, citizen=db_citizen, \
                                                            is_registered=citizen.is_registered)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_citizen_data = jsonable_encoder(updated_citizen)
        return json_compatible_citizen_data

    if db_citizen.user_id != citizen.user_id:
        updated_citizen = crud.update_citizen_user_id(db, citizen=db_citizen, \
                                                      user_id=citizen.user_id)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_citizen_data = jsonable_encoder(updated_citizen)
        return json_compatible_citizen_data
    return HTTPException(status_code=400, detail="Citizen is up to date")

# UPDATE client passport data
@router.put("/{citizen_id}/passport", response_model=schemas.ClientPassport, \
            status_code=200)
async def update_citizen_passport(passport: schemas.ClientPassport, \
                                 response: Response, \
                                 db=Depends(get_db)):
    db_passport = crud.get_citizen_passport_by_citizen_id(db, \
                                                          citizen_id=passport.citizen_id)
    if db_passport.passport_serial != passport.passport_serial:
        updated_passport = crud.update_citizen_passport_serial(db, \
                                                               serial=passport.passport_serial, \
                                                               passport=db_passport)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_citizen_passport_data = jsonable_encoder(updated_passport)
        return json_compatible_citizen_passport_data

    if db_passport.passport_number != passport.passport_number:
        updated_passport = crud.update_citizen_passport_number(db, \
                                                               number=passport.passport_number, \
                                                               passport=db_passport)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_citizen_passport_data = jsonable_encoder(updated_passport)
        return json_compatible_citizen_passport_data

    if db_passport.passport_date != passport.passport_date:
        updated_passport = crud.update_citizen_passport_date(db, \
                                                             passport_date=passport.passport_date, \
                                                             passport=db_passport)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_citizen_passport_data = jsonable_encoder(updated_passport)
        return json_compatible_citizen_passport_data

    if db_passport.passport_office != passport.passport_office:
        updated_passport = crud.update_citizen_passport_office(db, \
                                                               office=passport.passport_office, \
                                                               passport=db_passport)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_citizen_passport_data = jsonable_encoder(updated_passport)
        return json_compatible_citizen_passport_data

    if db_passport.is_active != passport.is_active:
        updated_passport = crud.update_citizen_passport_active_status(db, \
                                                                      status=passport.is_active, \
                                                                      passport=db_passport)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_citizen_passport_data = jsonable_encoder(updated_passport)
        return json_compatible_citizen_passport_data
    return HTTPException(status_code=400, detail="Citizen passport is up to date")

# DELETE client data
@router.delete("/{citizen_id}", status_code=200)
async def delete_citizen(citizen_id: int, db=Depends(get_db)):
    db_citizen = crud.get_citizen_by_citizen_id(db, citizen_id)
    if db_citizen is None:
        raise HTTPException(status_code=404, detail="Citizen not found")
    crud.delete_citizen(db, citizen_id)
    return f"Citizen {db_citizen.name} successfully deleted"

# DELETE client passport
@router.delete("/{citizen_id}/passport", status_code=200)
async def delete_citizen_passport(citizen_id: int, db=Depends(get_db)):
    db_passport = crud.get_citizen_passport_by_citizen_id(db, citizen_id)

    if db_passport is None:
        raise HTTPException(status_code=404, detail="Citizen passport not found")
    if not db_passport.is_active:
        raise HTTPException(status_code=400, detail="Citizen passport has active status: can't ba deleted!")
    crud.delete_citizen_passport(db, citizen_id)
    return f"Citizen by number {db_passport.citizen_id} passport sucsessfully deleted"

