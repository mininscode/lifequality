from fastapi import APIRouter, Depends, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from datetime import date

from database import SessionLocal, engine
from database.contracts import models, schemas, crud
from ..dependencies import get_token_header


models.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/contracts",
    tags=["contracts"],
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

# CREATE new contract
@router.post("/", response_model=schemas.Contract, status_code=200)
async def create_contract(contract: schemas.Contract, response: Response, \
                          db=Depends(get_db)):
    db_contract = crud.get_contract_by_id(db, contract_id=contract.id)
    if db_contract:
        raise HTTPException(status_code=400, \
                            detail="Contract already registered")
    response.status_code = status.HTTP_201_CREATED
    return crud.create_contract(db, contract)

# READ contracts data
@router.get("/", response_model=list[schemas.Contract], status_code=200)
async def read_contracts(db=Depends(get_db), skip: int = 0, limit: int = 100):
    db_contracts = crud.get_all_contracts(db, skip=skip, limit=limit)
    json_compatible_contacts_data = jsonable_encoder(db_contracts)
    return json_compatible_contacts_data

@router.get("/{contract_id}", response_model=schemas.Contract, status_code=200)
async def read_contract_by_id(contract_id: int, db=Depends(get_db)):
    db_contract = crud.get_contract_by_id(db, contract_id)
    json_compatible_contact_data = jsonable_encoder(db_contract)
    return json_compatible_contact_data

@router.get("/number/{contract_number}", response_model=schemas.Contract, \
            status_code=200)
async def read_contract_by_contract_number(contract_number: int, \
                                           db=Depends(get_db)):
    db_contract = crud.get_contract_by_contract_number(db, contract_number)
    json_compatible_contact_data = jsonable_encoder(db_contract)
    return json_compatible_contact_data

@router.get("/contracts_date/{contract_date}", \
            response_model=list[schemas.Contract], status_code=200)
async def read_contracts_by_contract_date(contract_date: date, \
                                          db=Depends(get_db), \
                                          skip: int = 0, \
                                          limit: int = 100):
    db_contracts = crud.get_contracts_by_contract_date(db, contract_date, \
                                                       skip=skip, limit=limit)
    json_compatible_contacts_data = jsonable_encoder(db_contracts)
    return json_compatible_contacts_data

@router.get("/expire_date/{expiration_date}", \
            response_model=list[schemas.Contract], status_code=200)
async def read_contracts_by_eexpiration_date(expiration_date: date, \
                                             db=Depends(get_db), \
                                             skip: int = 0, \
                                             limit: int = 100):
    db_contracts = crud.get_contracts_by_expiration_date(db, expiration_date, \
                                                         skip=skip, limit=limit)
    json_compatible_contacts_data = jsonable_encoder(db_contracts)
    return json_compatible_contacts_data

@router.get("/contractor/{contractor_id}", \
            response_model=list[schemas.Contract], status_code=200)
async def read_contracts_by_contractor_id(contractor_id: int, \
                                          db=Depends(get_db), \
                                          skip: int = 0, \
                                          limit: int = 100):
    db_contracts = crud.get_contracts_by_contractor_id(db, contractor_id, \
                                                       skip=skip, limit=limit)
    json_compatible_contacts_data = jsonable_encoder(db_contracts)
    return json_compatible_contacts_data

@router.get("/house/{house_id}", response_model=list[schemas.Contract], \
            status_code=200)
async def read_contracts_by_house_id(house_id: int, db=Depends(get_db), \
                                     skip: int = 0, limit: int = 100):
    db_contracts = crud.get_contracts_by_house_id(db, house_id, skip=skip, \
                                                  limit=limit)
    json_compatible_contacts_data = jsonable_encoder(db_contracts)
    return json_compatible_contacts_data

@router.get("/active_status/{is_active}", \
            response_model=list[schemas.Contract], status_code=200)
async def read_contracts_by_active_status(is_active: bool, db=Depends(get_db), \
                                          skip: int = 0, limit: int = 100):
    db_contracts = crud.get_contracts_by_active_status(db, is_active, \
                                                       skip=skip, limit=limit)
    json_compatible_contacts_data = jsonable_encoder(db_contracts)
    return json_compatible_contacts_data

# UPDATE contracts data
@router.put("/{contract_id}", response_model=schemas.Contract, status_code=200)
async def update_contract(contract: schemas.Contract, response: Response, \
                          db=Depends(get_db)):
    db_contract = crud.get_contract_by_id(db, contract_id=contract.id)

    if db_contract.contract_number != contract.contract_number:
        updated_contract = crud.update_contract_number(db, \
                                                       contract=db_contract, \
                                                       new_contract_number=\
                                                       contract.contract_number)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_contact_data = jsonable_encoder(updated_contract)
        return json_compatible_contact_data

    if db_contract.contract_date != contract.contract_date:
        updated_contract = crud.update_contract_contract_date(db, \
                                                              contract=\
                                                              db_contract, \
                                                              new_contract_date=\
                                                              contract.contract_date)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_contact_data = jsonable_encoder(updated_contract)
        return json_compatible_contact_data

    if db_contract.expiration_date != contract.expiration_date:
        updated_contract = crud.update_contract_expiration_date(db, \
                                                                contract=\
                                                                db_contract, \
                                                                new_expiration_date=\
                                                                contract.expiration_date)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_contact_data = jsonable_encoder(updated_contract)
        return json_compatible_contact_data

    if db_contract.contractor_id != contract.contractor_id:
        updated_contract = crud.update_contract_contractor_id(db, \
                                                              contract=\
                                                              db_contract, \
                                                              new_contractor_id=\
                                                              contract.contractor_id)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_contact_data = jsonable_encoder(updated_contract)
        return json_compatible_contact_data

    if db_contract.house_id != contract.house_id:
        updated_contract = crud.update_contract_house_id(db, \
                                                         contract=db_contract, \
                                                         new_house_id=\
                                                         contract.house_id)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_contact_data = jsonable_encoder(updated_contract)
        return json_compatible_contact_data

    if db_contract.is_active != contract.is_active:
        updated_contract = crud.update_contract_active_status(db, \
                                                              contract=\
                                                              db_contract, \
                                                              status=\
                                                              contract.is_active)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_contact_data = jsonable_encoder(updated_contract)
        return json_compatible_contact_data
    return HTTPException(status_code=400, detail="Contract is up to date")

# DELEETE contract
@router.delete("/{contract_id}", status_code=200)
async def delete_contract(contract_id: int, db=Depends(get_db)):
    db_contract = crud.get_contract_by_id(db, contract_id)
    if db_contract is None:
        raise HTTPException(status_code=400, detail="Contract not found")
    crud.delete_contract(db, contract_id)
    return f"Contract {contract_id} successfully deleted"

