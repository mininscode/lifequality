from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.encoders import jsonable_encoder

from database import SessionLocal, engine
from database.contractors import models, schemas, crud
from ..dependencies import get_token_header

models.Base.metadata.create_all(bind=engine)

router=APIRouter(
    prefix="/contractors",
    tags=["contractors"],
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

# CREATE new contractor
@router.post("/", response_model=schemas.Contractor, status_code=200)
async def create_contractor(contractor: schemas.Contractor, response: Response, \
                            db=Depends(get_db)):
    db_contractor = crud.get_contractor_by_id(db, contractor_id=contractor.id)
    if db_contractor:
        raise HTTPException(status_code=400, \
                            detail="Contractor already registered")
    response.status_code = status.HTTP_201_CREATED
    return crud.create_contractor(db, contractor)

# READ contractors data
@router.get("/", response_model=list[schemas.Contractor], status_code=200)
async def read_contractors(db=Depends(get_db), skip: int = 0, limit: int = 100):
    db_contractors = crud.get_all_contractors(db, skip=skip, limit=limit)
    json_compatible_contractors_data = jsonable_encoder(db_contractors)
    return json_compatible_contractors_data

@router.get("/{contractor_id}", response_model=schemas.Contractor, status_code=200)
async def read_contractor(contractor_id: int, db=Depends(get_db)):
    db_contractor = crud.get_contractor_by_id(db, contractor_id)
    json_compatible_contractor_data = jsonable_encoder(db_contractor)
    return json_compatible_contractor_data

@router.get("/name/{contractor_name}", response_model=schemas.Contractor, \
            status_code=200)
async def read_contractor_by_name(contractor_name: str, db=Depends(get_db)):
    db_contractor = crud.get_contractor_by_name(db, contractor_name)
    json_compatible_contractor_data = jsonable_encoder(db_contractor)
    return json_compatible_contractor_data

@router.get("/user/{user_id}", response_model=schemas.Contractor, status_code=200)
async def read_contractor_by_user_id(user_id: int, db=Depends(get_db)):
    db_contractor = crud.get_contractor_by_user_id(db, user_id)
    json_compatible_contractor_data = jsonable_encoder(db_contractor)
    return json_compatible_contractor_data

@router.get("/emergency/{emergency_service_status}", \
            response_model=list[schemas.Contractor], \
            status_code=200)
async def read_contractos_by_emergency_service_status(emergency_status: bool, \
                                                      db=Depends(get_db), \
                                                      skip: int = 0, \
                                                      limit: int = 100):
    db_contractors = crud.get_contractors_by_emergency_service_status(db, \
                                                                      emergency_status, \
                                                                      skip=skip, \
                                                                      limit=limit)
    json_compatible_contractors_data = jsonable_encoder(db_contractors)
    return json_compatible_contractors_data



# UPDATE contractors data
@router.put("/{contractor_id}", response_model=schemas.Contractor, \
        status_code=200)
async def update_contractor(contractor: schemas.Contractor, \
                            response: Response, db=Depends(get_db)):
    db_contractor = crud.get_contractor_by_id(db, contractor_id=contractor.id)

    if db_contractor.name != contractor.name:
        updated_contractor = crud.update_contractor_name(db, \
                                                         contractor=db_contractor, \
                                                         new_name=contractor.name)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_contractor_data = jsonable_encoder(updated_contractor)
        return json_compatible_contractor_data

    if db_contractor.city != contractor.city:
        updated_contractor = crud.update_contractor_city(db, \
                                                         contractor=db_contractor, \
                                                         new_city=contractor.city)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_contractor_data = jsonable_encoder(updated_contractor)
        return json_compatible_contractor_data

    if db_contractor.street != contractor.street:
        updated_contractor = crud.update_contractor_street(db, \
                                                           contractor=db_contractor, \
                                                           new_street=contractor.street)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_contractor_data = jsonable_encoder(updated_contractor)
        return json_compatible_contractor_data

    if db_contractor.building != contractor.building:
        updated_contractor = crud.update_contractor_building(db, \
                                                             contractor=db_contractor, \
                                                             new_building=contractor.building)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_contractor_data = jsonable_encoder(updated_contractor)
        return json_compatible_contractor_data

    if db_contractor.contract_id != contractor.contract_id:
        updated_contractor = crud.update_contractor_contract_id(db, \
                                                                contractor=db_contractor, \
                                                                new_contract_id=contractor.contract_id)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_contractor_data = jsonable_encoder(updated_contractor)
        return json_compatible_contractor_data

    if db_contractor.user_id != contractor.user_id:
        updated_contractor = crud.update_contractor_user_id(db, \
                                                            contractor=db_contractor, \
                                                            new_user_id=contractor.user_id)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_contractor_data = jsonable_encoder(updated_contractor)
        return json_compatible_contractor_data

    if db_contractor.is_emergency_service != contractor.is_emergency_service:
        updated_contractor = crud.update_contractor_emergency_status(db, \
                                                                     contractor=db_contractor, \
                                                                     new_emergency_status=contractor.is_emergency_service)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_contractor_data = jsonable_encoder(updated_contractor)
        return json_compatible_contractor_data
    return HTTPException(status_code=400, detail="Contractor is up to date")

# DELETE contractor
@router.delete("/{contractor_id}", status_code=200)
async def delete_contractor(contractor_id: int, db=Depends(get_db)):
    db_contractor = crud.get_contractor_by_id(db, contractor_id)
    if db_contractor is None:
        raise HTTPException(status_code=400, detail="Contractor not found")
    crud.delete_contractor(db, contractor_id)
    return f"Contractor {contractor_id} successfully deleted"

