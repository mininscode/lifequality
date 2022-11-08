from fastapi import APIRouter, HTTPException, Depends, Response, status
from fastapi.encoders import jsonable_encoder
from datetime import datetime

from database import SessionLocal, engine
from database.comments import models, schemas, crud
from ..dependencies import get_token_header


models.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/comments",
    tags=["comments"],
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

# CREATE new comment
@router.post("/", response_model=schemas.Comment, status_code=200)
async def create_comment(comment: schemas.Comment, response: Response, \
                         db=Depends(get_db)):
    db_comment = crud.get_comment_by_id(db, comment_id=comment.id)
    if db_comment:
        raise HTTPException(status_code=400, \
                            detail="Comment already registered")
    response.status_code = status.HTTP_201_CREATED
    return crud.create_comment(db, comment)

# READ comments data
@router.get("/", response_model=list[schemas.Comment], status_code=200)
async def read_comments(db=Depends(get_db), skip: int = 0, limit: int = 100):
    db_comments = crud.get_all_comments(db, skip=skip, limit=limit)
    json_compatible_comments_data = jsonable_encoder(db_comments)
    return json_compatible_comments_data

@router.get("/{comment_id}", response_model=schemas.Comment, status_code=200)
async def read_comment(comment_id: int, db=Depends(get_db)):
    db_comment = crud.get_comment_by_id(db, comment_id)
    json_compatible_comment_data = jsonable_encoder(db_comment)
    return json_compatible_comment_data

@router.get("/author/{author_id}", response_model=list[schemas.Comment], \
            status_code=200)
async def read_comments_by_author_id(author_id: int, db=Depends(get_db), \
                                     skip: int = 0, limit: int = 100):
    db_comments = crud.get_comments_by_author_id(db, \
                                                 author_id, \
                                                 skip = skip, \
                                                 limit = limit)
    json_compatible_comments_data = jsonable_encoder(db_comments)
    return json_compatible_comments_data

@router.get("/created/{created_at}", response_model=list[schemas.Comment], \
            status_code=200)
async def read_comments_by_created_at(created_at: datetime, \
                                      db=Depends(get_db), \
                                      skip: int = 0, \
                                      limit: int = 100):
    db_comments = crud.get_comments_by_created_at(db, \
                                                  created_at, \
                                                  skip = skip, \
                                                  limit = limit)
    json_compatible_comments_data = jsonable_encoder(db_comments)
    return json_compatible_comments_data

@router.get("/citizen_request/{request_id}", \
            response_model=list[schemas.Comment], status_code=200)
async def read_comments_by_citizen_request_id(request_id: int, \
                                              db=Depends(get_db), \
                                              skip: int = 0, \
                                              limit: int = 100):
    db_comments = crud.get_comments_by_citizen_request_id(db, \
                                                          request_id, \
                                                          skip = skip, \
                                                          limit = limit)
    json_compatible_comments_data = jsonable_encoder(db_comments)
    return json_compatible_comments_data

# UPDATE comments data
@router.put("/{comment_id}", response_model=schemas.Comment, status_code=200)
async def update_comment(comment: schemas.Comment, \
                         response: Response, \
                         db=Depends(get_db)):
    db_comment = crud.get_comment_by_id(db, comment_id=comment.id)

    if db_comment.text != comment.text:
        updated_comment = crud.update_comment_text(db, comment=db_comment, \
                                                   new_text=comment.text)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_comment_data = jsonable_encoder(updated_comment)
        return json_compatible_comment_data

    if db_comment.author_id != comment.author_id:
        updated_comment = crud.update_comment_author_id(db, \
                                                        comment=db_comment, \
                                                        new_author_id=\
                                                        comment.author_id)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_comment_data = jsonable_encoder(updated_comment)
        return json_compatible_comment_data

    if db_comment.created_at != comment.created_at:
        updated_comment = crud.update_comment_create_date(db, \
                                                          comment=db_comment, \
                                                          created_at=\
                                                          comment.created_at)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_comment_data = jsonable_encoder(updated_comment)
        return json_compatible_comment_data

    if db_comment.citizen_request_id != comment.citizen_request_id:
        updated_comment = crud.update_comment_citizen_request_id(db, \
                                                                 comment=\
                                                                 db_comment, \
                                                                 citizen_request_id=\
                                                                 comment.citizen_request_id)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_comment_data = jsonable_encoder(updated_comment)
        return json_compatible_comment_data
    return HTTPException(status_code=400, detail="Comment is up to date")

# DELETE comment
@router.delete("/{comment_id}", status_code=200)
async def delete_comment(comment_id: int, db=Depends(get_db)):
    db_comment = crud.get_comment_by_id(db, comment_id)
    if db_comment is None:
        raise HTTPException(status_code=400, detail="Comment not found")
    crud.delete_comment(db, comment_id)
    return f"Comment {comment_id} successfully deleted"

