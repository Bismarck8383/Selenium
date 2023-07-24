from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import *


router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/all_employees")
def get_all_employees(db: Session = Depends(get_db)):
    employees = db.query(Employee).all()
    return [employee.to_dict() for employee in employees]


@router.get("/employees/{employee_id}")
def get_employee_by_id(employee_id: int, db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    return employee.to_dict()


@router.get("/employees_filters")
def get_employees_todos(city: str = None, cargo: str = None, db: Session = Depends(get_db)):
    query = db.query(Employee)
    if city and not cargo:
        query = query.filter(Employee.ciudad.like(f"%{city}%"))
    elif cargo and not city:
        query = query.filter(Employee.cargo.like(f"%{cargo}%"))
    elif city and cargo:
        query = query.filter(Employee.ciudad.like(f"%{city}%"), Employee.cargo.like(f"%{cargo}%"))
    employees = query.all()
    return [employee.to_dict() for employee in employees]


@router.post("/create_employee")
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    new_employee = Employee(
        name=employee.name,
        email=employee.email,
        ciudad=employee.ciudad,
        cargo=employee.cargo,
        edad=employee.edad,
        fecha_contratacion=employee.fecha_contratacion,
        salario=employee.salario,
        telefono=employee.telefono,
        direccion=employee.direccion,
        genero=employee.genero
    )
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return new_employee.to_dict()


@router.put("/employee_update/{employee_id}")
def update_employee(employee_id: int, employee: EmployeeUpdate, db: Session = Depends(get_db)):
    existing_employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not existing_employee:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")

    # Actualizar los campos del empleado existente con los nuevos valores
    existing_employee.name = employee.name
    existing_employee.email = employee.email
    existing_employee.ciudad = employee.ciudad
    existing_employee.cargo = employee.cargo
    existing_employee.edad = employee.edad
    existing_employee.fecha_contratacion = employee.fecha_contratacion
    existing_employee.salario = employee.salario
    existing_employee.telefono = employee.telefono
    existing_employee.direccion = employee.direccion
    existing_employee.genero = employee.genero

    db.commit()
    db.refresh(existing_employee)
    return existing_employee.to_dict()


# Ruta para eliminar un empleado por su ID
@router.delete("/delete_employee/{employee_id}")
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")

    db.delete(employee)
    db.commit()
    return {"message": "Empleado eliminado correctamente"}
