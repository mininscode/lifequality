"""This module contains CRUD methods for Employee model"""

from sqlalchemy.orm import Session

from database.employees import models, schemas
from validation_types import FullNameType


# CREATE data in database
def create_employee(db: Session, employee: schemas.Employee):
    db_employee = models.Employee(
        name=employee.name,
        surname=employee.surname,
        patronymic=employee.patronymic,
        department=employee.department,
        position=employee.position,
        employee_number=employee.employee_number,
        user_id=employee.user_id
    )
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

# READ data from database
def get_employee_by_employee_number(db: Session, employee_number: int):
    return db.query(models.Employee).filter(\
           models.Employee.employee_number == employee_number).first()

def get_employee_by_fullname(db: Session, fullname: FullNameType):
    name = fullname['name']
    surname = fullname['surname']
    patronymic = fullname['patronymic']

    return db.query(models.Employee).filter(\
           models.Employee.name == name).filter(\
           models.Employee.surname == surname).filter(\
           models.Employee.patronymic == patronymic).first()

def get_employee_by_user_id(db: Session, user_id: int):
    return db.query(models.Employee).filter(models.Employee.user_id == \
           user_id).first()

def get_all_employees_by_name(db: Session, name: str, \
                              skip: int = 0, limit: int = 100):
    return db.query(models.Employee).filter(models.Employee.name == \
           name).offset(skip).limit(limit).all()

def get_all_employees_by_surname(db: Session, surname: str, \
                                 skip: int = 0, limit: int = 100):
    return db.query(models.Employee).filter(models.Employee.surname == \
           surname).offset(skip).limit(limit).all()

def get_all_employees_by_patronymic(db: Session, patronymic: str, \
                                    skip: int = 0, limit: int = 100):
    return db.query(models.Employee).filter(models.Employee.patronymic == \
           patronymic).offset(skip).limit(limit).all()

def get_all_employees_by_department(db: Session, department: str, \
                                    skip: int = 0, limit: int = 100):
    return db.query(models.Employee).filter(models.Employee.department == \
           department).offset(skip).limit(limit).all()

def get_all_empoyees_by_position(db: Session, position: str, \
                                 skip: int = 0, limit: int = 100):
    return db.query(models.Employee).filter(models.Employee.position == \
           position).offset(skip).limit(limit).all()

def get_all_employees(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Employee).offset(skip).limit(limit).all()

# UPDATE data in database
def update_employee_name(db: Session, employee_number: int, name: str):
    db_employee = get_employee_by_employee_number(db, employee_number)
    db_employee.name = name
    db.commit()
    db.refresh(db_employee)
    return db_employee

def update_employee_surname(db: Session, employee_number: int, surname: str):
    db_employee = get_employee_by_employee_number(db, employee_number)
    db_employee.surname = surname
    db.commit()
    db.refresh(db_employee)
    return db_employee

def update_employee_patronymic(db: Session, employee_number: int, \
                               patronymic: str):
    db_employee = get_employee_by_employee_number(db, employee_number)
    db_employee.patronymic = patronymic
    db.commit()
    db.refresh(db_employee)
    return db_employee

def update_employee_department(db: Session, employee_number: int, \
                               department: str):
    db_employee = get_employee_by_employee_number(db, employee_number)
    db_employee.department = department
    db.commit()
    db.refresh(db_employee)
    return db_employee

def update_employee_position(db: Session, employee_number: int, position: str):
    db_employee = get_employee_by_employee_number(db, employee_number)
    db_employee.position = position
    db.commit()
    db.refresh(db_employee)
    return db_employee

def update_employee_employee_number(db: Session, \
                                    employee_number_current: int, \
                                    employee_number_new: int):
    db_employee = get_employee_by_employee_number(db, employee_number_current)
    db_employee.employee_number = employee_number_new
    db.commit()
    db.refresh(db_employee)
    return db_employee

def update_employee_user_id(db: Session, user_id_current: int, \
                            user_id_new: int):
    db_employee = get_employee_by_user_id(db, user_id_current)
    db_employee.user_id = user_id
    db.commit()
    db.refresh(db_employee)
    return db_employee

# DELETE data from database
def delete_employee(db: Session, employee_number: int):
    db_employee = get_employee_by_employee_number(db, employee_number)
    db.delete(db_employee)
    db.commit()

