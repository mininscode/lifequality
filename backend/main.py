from fastapi import FastAPI, Depends

from .dependencies import get_token_header, get_query_token
from .routers import users, clients, employees, contractors, call_records, \
                     client_requests, comments, consultations, contracts, \
                     house_conditions, houses, likes, meetings, \
                     request_documents, request_sources, request_statuses, \
                     works

app = FastAPI(dependencies=[Depends(get_query_token)])

app.include_router(users.router)
app.include_router(clients.router)
app.include_router(employees.router)
app.include_router(contractors.router)
app.include_router(call_records.router)
app.include_router(client_requests.router)
app.include_router(comments.router)
app.include_router(consultations.router)
app.include_router(contracts.router)
app.include_router(house_conditions.router)
app.include_router(houses.router)
app.include_router(likes.router)
app.include_router(meetings.router)
app.include_router(request_documents.router)
app.include_router(request_sources.router)
app.include_router(request_statuses.router)
app.include_router(works.router)

@app.get("/")
async def root():
    return {"message": "Hello Bigger Application!"}

