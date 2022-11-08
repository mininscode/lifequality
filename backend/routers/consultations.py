from fastapi import APIRouter, HTTPException, Depends, Response, status
from fastapi.encoders import jsonable_encoder
from datetime import datetime

from database import SessionLocal, engine
from database.consultations import models, schemas, crud
from ..dependencies import get_token_header


models.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/consultations",
    tags=["consultations"],
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

# CREATE new consultation
@router.post("/", response_model=schemas.Consultation, status_code=200)
async def create_consultation(consultation: schemas.Consultation, \
                              response: Response, db=Depends(get_db)):
    db_consultation = crud.get_consultation_by_id(db, \
                                                  consultation_id=\
                                                  consultation.id)
    if db_consultation:
        raise HTTPException(status_code=400, \
                            detail="Consultation already registered")
    response.status_code = status.HTTP_201_CREATED
    return crud.create_consultation(db, consultation)

# READ consultations data
@router.get("/", response_model=list[schemas.Consultation], status_code=200)
async def read_consultations(db=Depends(get_db), skip: int = 0, \
                             limit: int = 100):
    db_consultations = crud.get_all_consultations(db, skip=skip, limit=limit)
    json_compatible_consultations_data = jsonable_encoder(db_consultations)
    return json_compatible_consultations_data

@router.get("/{consultation_id}", response_model=schemas.Consultation, \
            status_code=200)
async def read_consultation(consultation_id: int, db=Depends(get_db)):
    db_consultation = crud.get_consultation_by_id(db, consultation_id)
    json_compatible_consultation_data = jsonable_encoder(db_consultation)
    return json_compatible_consultation_data

@router.get("/create_date/{created_at}", \
            response_model=list[schemas.Consultation], status_code=200)
async def read_consultations_by_create_date(created_at: datetime, \
                                            db=Depends(get_db), \
                                            skip: int = 0, \
                                            limit: int = 100):
    db_consultations = crud.get_consultations_by_create_date(db, \
                                                             created_at, \
                                                             skip=skip, \
                                                             limit=limit)
    json_compatible_consultations_data = jsonable_encoder(db_consultations)
    return json_compatible_consultations_data

@router.get("/citizen/{citizen_id}", \
            response_model=list[schemas.Consultation], status_code=200)
async def read_consultations_by_citizen_id(citizen_id: int, \
                                            db=Depends(get_db), \
                                            skip: int = 0, \
                                            limit: int = 100):
    db_consultations = crud.get_consultations_by_citizen_id(db, \
                                                            citizen_id, \
                                                            skip=skip, \
                                                            limit=limit)
    json_compatible_consultations_data = jsonable_encoder(db_consultations)
    return json_compatible_consultations_data

# UPDATE consultation data
@router.put("/{consultation_id}", response_model=schemas.Consultation, \
            status_code=200)
async def update_consultation(consultation: schemas.Consultation, \
                              response: Response, db=Depends(get_db)):
    db_consultation = crud.get_consultation_by_id(db, \
                                                  consultation_id=\
                                                  consultation.id)
    if db_consultation.created_at != consultation.created_at:
        updated_consultation = crud.update_consultation_create_date(db, \
                                                                    consultation=\
                                                                    db_consultation, \
                                                                    created_at=\
                                                                    consultation.created_at)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_consultation_data = jsonable_encoder(updated_consultation)
        return json_compatible_consultation_data

    if db_consultation.text != consultation.text:
        updated_consultation = crud.update_consultation_text(db, \
                                                              consultation=\
                                                              db_consultation, \
                                                              new_text=\
                                                              consultation.text)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_consultation_data = jsonable_encoder(updated_consultation)
        return json_compatible_consultation_data

    if db_consultation.citizen_id != consultation.citizen_id:
        updated_consultation = crud.update_consultation_citizen_id(db, \
                                                                   consultation=\
                                                                   db_consultation, \
                                                                   citizen_id=\
                                                                   consultation.citizen_id)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_consultation_data = jsonable_encoder(updated_consultation)
        return json_compatible_consultation_data

# DELETE consultation
@router.delete("/{consultation_id}", status_code=200)
async def delte_consultation(consultation_id: int, db=Depends(get_db)):
    db_consultation = crud.get_consultation_by_id(db, consultation_id)
    if db_consultation is None:
        raise HTTPException(status_code=400, detail="Consultation not found")
    crud.delete_consultation(db, consultation_id)
    return f"Consultation {consultation_id} successfully deleted"

