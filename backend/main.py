from fastapi import FastAPI, Depends

from .dependencies import get_token_header, get_query_token
from .routers import users

app = FastAPI(dependencies=[Depends(get_query_token)])

app.include_router(users.router)

@app.get("/")
async def root():
    return {"message": "Hello Bigger Application!"}

