from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.encoders import jsonable_encoder
from datetime import datetime
from typing import Literal

from database import SessionLocal, engine
from database.request_documents import models, schemas, crud
from ..dependencies import get_token_header


models.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/request_documents",
    tags=["request_documents"],
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

# CREATE new request document
@router.post("/", response_model=schemas.RequestDocument, status_code=200)
async def create_request_document(document: schemas.RequestDocument, \
                                  response: Response, db=Depends(get_db)):
    db_document = crud.get_request_document_by_id(db, document_id=document.id)
    if db_document:
        raise HTTPException(status_code=400, \
                            detail="Document already registered")
    response.status_code = status.HTTP_201_CREATED
    return crud.create_request_document(db, document)

# READ request document data
@router.get("/", response_model=list[schemas.RequestDocument], status_code=200)
async def read_request_documents(db=Depends(get_db), skip: int = 0, \
                                 limit: int = 100):
    db_documents = crud.get_all_request_documents(db, skip=skip, limit=limit)
    json_compatible_request_documents_data = jsonable_encoder(db_documents)
    return json_compatible_request_documents_data

@router.get("/{document_id}", response_model=schemas.RequestDocument, \
            status_code=200)
async def read_request_document_by_id(document_id: int, db=Depends(get_db)):
    db_document = crud.get_request_document_by_id(db, document_id)
    json_compatible_request_document_data = jsonable_encoder(db_document)
    return json_compatible_request_document_data

@router.get("/document_type/{document_type}", \
            response_model=list[schemas.RequestDocument], status_code=200)
async def read_request_documents_by_type(document_type: \
                                         Literal["act", "document", \
                                                 "photo", "video"], \
                                         db=Depends(get_db), \
                                         skip: int = 0, \
                                         limit: int = 100):
    db_documents = crud.get_request_documents_by_document_type(db, \
                                                               document_type, \
                                                               skip=skip, \
                                                               limit=limit)
    json_compatible_request_documents_data = jsonable_encoder(db_documents)
    return json_compatible_request_documents_data

@router.get("/create_date/{created_at}", \
            response_model=list[schemas.RequestDocument], status_code=200)
async def read_request_documents_by_create_date(created_at: datetime, \
                                                db=Depends(get_db), \
                                                skip: int = 0, \
                                                limit: int = 100):
    db_documents = crud.get_request_documents_by_created_at(db, \
                                                            created_at, \
                                                            skip=skip, \
                                                            limit=limit)
    json_compatible_request_documents_data = jsonable_encoder(db_documents)
    return json_compatible_request_documents_data

@router.get("/citizen_requet/{request_id}", \
            response_model=list[schemas.RequestDocument], status_code=200)
async def read_request_documents_by_citizen_request_id(request_id: int, \
                                                       db=Depends(get_db), \
                                                       skip: int = 0, \
                                                       limit: int = 100):
    db_documents = crud.get_request_documents_by_request_id(db, request_id, \
                                                            skip=skip, \
                                                            limit=limit)
    json_compatible_request_documents_data = jsonable_encoder(db_documents)
    return json_compatible_request_documents_data

@router.get("/contractor/{contractor_id}", \
            response_model=list[schemas.RequestDocument], status_code=200)
async def read_request_documents_by_contract_id(contractor_id: int, \
                                                db=Depends(get_db), \
                                                skip: int = 0, \
                                                limit: int = 100):
    db_documents = crud.get_request_documents_by_contractor_id(db, \
                                                               contractor_id, \
                                                               skip=skip, \
                                                               limit=limit)
    json_compatible_request_documents_data = jsonable_encoder(db_documents)
    return json_compatible_request_documents_data

# UPDATE request document
@router.put("/{document_id}", response_model=schemas.RequestDocument, \
            status_code=200)
async def update_request_document(document: schemas.RequestDocument, \
                                  response: Response, db=Depends(get_db)):
    db_document = crud.get_request_document_by_id(db, document_id=document.id)

    if db_document.document_type != document.document_type:
        updated_document = crud.update_document_type(db, \
                                                     document=\
                                                     db_document, \
                                                     document_type=\
                                                     document.document_type)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_document_data = jsonable_encoder(updated_document)
        return json_compatible_document_data

    if db_document.file_path != document.file_path:
        updated_document = crud.update_document_file_path(db, \
                                                          document=\
                                                          db_document, \
                                                          new_file_path=\
                                                          document.file_path)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_document_data = jsonable_encoder(updated_document)
        return json_compatible_document_data

    if db_document.created_at != document.created_at:
        updated_document = crud.update_document_create_date(db, \
                                                            document=\
                                                            db_document, \
                                                            created_at=\
                                                            document.created_at)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_document_data = jsonable_encoder(updated_document)
        return json_compatible_document_data

    if db_document.citizen_request_id != document.citizen_request_id:
        updated_document = crud.update_document_citizen_request_id(db, \
                                                                   document=\
                                                                   db_document, \
                                                                   citizen_request_id=\
                                                                   document.citizen_request_id)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_document_data = jsonable_encoder(updated_document)
        return json_compatible_document_data

    if db_document.contractor_id != document.contractor_id:
        updated_document = crud.update_document_contractor_id(db, \
                                                              document=\
                                                              db_document, \
                                                              contractor_id=\
                                                              document.contractor_id)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_document_data = jsonable_encoder(updated_document)
        return json_compatible_document_data
    return HTTPException(status_code=400, \
                         detail="Request document is up to date")

# DELETE request document
@router.delete("/{document_id}", status_code=200)
async def delete_request_document(document_id: int, db=Depends(get_db)):
    db_document = crud.get_request_document_by_id(db, document_id)
    if db_document is None:
        raise HTTPException(status_code=400, \
                            detail="Request document not found")
    crud.delete_request_document(db, document_id)
    return f"Request document {document_id} successfully deleted"

