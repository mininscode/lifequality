from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.encoders import jsonable_encoder

from database import SessionLocal, engine
from database.employees import models, schemas, crud
from ..dependencies import get_token_header

models.Base.metadata.create_all(bind=engine)

router = APIRouter(
    prefix="/employees",
    tags=["employees"],
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

# CREATE new employee
@router.post("/", response_model=schemas.Employee, status_code=200)
async def create_employee(employee: schemas.Employee, response: Response, \
                          db=Depends(get_db)):
    db_employee = crud.get_employee_by_user_id(db, user_id=employee.user_id)
    if db_employee:
        raise HTTPException(status_code=400, \
                            detail="Employee already registered")
    response.status_code = status.HTTP_201_CREATED
    return crud.create_employee(db, employee)

# READ employees data
@router.get("/", response_model=list[schemas.Employee], status_code=200)
async def read_employees(db=Depends(get_db), skip: int = 0, limit: int = 100):
    db_employees = crud.get_all_employees(db, skip=skip, limit=limit)
    json_compatible_employees_data = jsonable_encoder(db_employees)
    return json_compatible_employees_data

@router.get("/name/{employee_name}", response_model=list[schemas.Employee], \
            status_code=200)
async def read_employees_by_name(name: str, db=Depends(get_db), skip: int = 0, \
                                 limit: int = 100):
    db_employees = crud.get_all_employees_by_name(db, name=name, skip=skip, \
                                                  limit=limit)
    json_compatible_employees_data = jsonable_encoder(db_employees)
    return json_compatible_employees_data

@router.get("/surname/{employee_surname}", response_model=list[schemas.Employee], \
            status_code=200)
async def read_employees_by_surname(surname: str, db=Depends(get_db), \
                                    skip: int = 0, limit: int = 100):
    db_employees = crud.get_all_employees_by_surname(db, surname=surname, \
                                                 skip=skip, limit=limit)
    json_compatible_employees_data = jsonable_encoder(db_employees)
    return json_compatible_employees_data

@router.get("/patronymic/{employee_patronymic}", response_model=list[schemas.Employee], \
            status_code=200)
async def read_employees_by_patronymic(patronymic: str, db=Depends(get_db), \
                                       skip: int = 0, limit: int = 100):
    db_employees = crud.get_all_employees_by_patronymic(db, patronymic=patronymic, \
                                                        skip=skip, limit=limit)
    json_compatible_employees_data = jsonable_encoder(db_employees)
    return json_compatible_employees_data

@router.get("/department/{employee_department}", response_model=list[schemas.Employee], \
            status_code=200)
async def read_employees_by_department(department: str, db=Depends(get_db), \
                                       skip: int = 0, limit: int = 100):
    db_employees = crud.get_all_employees_by_department(db, department=department, \
                                                        skip=skip, limit=limit)
    json_compatible_employees_data = jsonable_encoder(db_employees)
    return json_compatible_employees_data

@router.get("/position/{employees_position}", response_model=list[schemas.Employee], \
            status_code=200)
async def read_employees_by_position(position: str, db=Depends(get_db), \
                                     skip: int = 0, limit: int = 100):
    db_employees = crud.get_all_employees_by_position(db, position=position, \
                                                        skip=skip, limit=limit)
    json_compatible_employees_data = jsonable_encoder(db_employees)
    return json_compatible_employees_data

@router.get("/employee_number/{employee_number}", \
            response_model=schemas.Employee, \
            status_code=200)
async def read_employee_by_employee_number(number: int, db=Depends(get_db)):
    db_employee = crud.get_employee_by_employee_number(db, employee_number=number)
    json_compatible_employee_data = jsonable_encoder(db_employee)
    return json_compatible_employee_data

@router.get("/{user_id}", response_model=schemas.Employee, status_code=200)
async def read_eemployee_by_user_id(user_id: int, db=Depends(get_db)):
    db_employee = crud.get_employee_by_user_id(db, user_id=user_id)
    json_compatible_employee_data = jsonable_encoder(db_employee)
    return json_compatible_employee_data

# UPDATE employees data
@router.put("/{user_id}", response_model=schemas.Employee, status_code=200)
async def update_employee(employee: schemas.Employee, response: Response, \
                          db=Depends(get_db)):
    db_employee = crud.get_employee_by_user_id(db, user_id=employee.user_id)

    if db_employee.name != employee.name:
        updated_employee = crud.update_employee_name(db, \
                                                       employee=db_employee, \
                                                       name=employee.name)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_employee_data = jsonable_encoder(updated_employee)
        return json_compatible_employee_data

    if db_employee.surname != employee.surname:
        updated_employee = crud.update_employee_surname(db, \
                                                        employee=db_employee, \
                                                        surname=employee.surname)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_employee_data = jsonable_encoder(updated_employee)
        return json_compatible_employee_data

    if db_employee.patronymic != employee.patronymic:
        updated_employee = crud.update_employee_patronymic(db, \
                                                           employee=db_employee, \
                                                           patronymic=\
                                                           employee.patronymic)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_employee_data = jsonable_encoder(updated_employee)
        return json_compatible_employee_data

    if db_employee.department != employee.department:
        updated_employee = crud.update_employee_department(db, \
                                                           employee=db_employee, \
                                                           department=\
                                                           employee.department)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_employee_data = jsonable_encoder(updated_employee)
        return json_compatible_employee_data

    if db_employee.position != employee.position:
        updated_employee = crud.update_employee_position(db, employee=db_employee, \
                                                         position=employee.position)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_employee_data = jsonable_encoder(updated_employee)
        return json_compatible_employee_data

    if db_employee.employee_number != employee.employee_number:
        updated_employee = crud.update_employee_employee_number(db, \
                                                                employee=db_employee, \
                                                                new_employee_number=\
                                                                employee.employee_number)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_employee_data = jsonable_encoder(updated_employee)
        return json_compatible_employee_data

    if db_employee.user_id != employee.user_id:
        updated_employee = crud.update_employee_user_id(db, \
                                                        employee=db_employee, \
                                                        new_user_id=\
                                                        employee.user_id)
        response.status_code = status.HTTP_201_CREATED
        json_compatible_employee_data = jsonable_encoder(updated_employee)
        return json_compatible_employee_data
    return HTTPException(status_code=400, detail="Employee is up to date")

# DELETE employee data
@router.delete("/{employee_number}", status_code=200)
async def delete_employee(employee_number: int, db=Depends(get_db)):
    db_employee = crud.get_employee_by_employee_number(db, employee_number)
    if db_employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    crud.delete_employee(db, employee_number)
    return f"Employee {employee_number} successfully deleted"

