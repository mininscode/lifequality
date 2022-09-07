from fastapi import Header, HTTPException


async def get_token_header(x_token: str = Header(default='super_secret_token')):
    if x_token != "super_secret_token": #TODO: add real token generation
        raise HTTPException(status_code=400, detail="X-token header invalid")

async def get_query_token(token: str):
    if token != "some_token": #TODO: add real token generation
        raise HTTPException(status_code=400, detail="No some_token provided")

