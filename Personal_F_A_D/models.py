from sqlalchemy import Column, Integer, String, Date, Float
from database import Base
from pydantic import BaseModel, validator
from datetime import date
from pydantic import BaseSettings


class Settings(BaseSettings):
    arbitrary_types_allowed = True


conf = Settings()


def date_to_str(date_value):
    if date_value is None:
        return None
    return date_value.isoformat()


class Employee(Base):
    __tablename__ = 'employee'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    ciudad = Column(String(100), nullable=False)
    edad = Column(Integer, nullable=False)
    cargo = Column(String(100), nullable=False)
    fecha_contratacion = Column(Date, nullable=True)
    salario = Column(Float, nullable=True)
    telefono = Column(String(15), nullable=True)
    direccion = Column(String(100), nullable=True)
    genero = Column(String(10), nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "ciudad": self.ciudad,
            "edad": self.edad,
            "cargo": self.cargo,
            "fecha_contratacion": self.fecha_contratacion,
            "salario": self.salario,
            "telefono": self.telefono,
            "direccion": self.direccion,
            "genero": self.genero
        }


class EmployeeCreate(BaseModel):
    name: str
    email: str
    ciudad: str
    cargo: str
    edad: int
    fecha_contratacion: date
    salario: float
    telefono: str
    direccion: str
    genero: str

    @validator('fecha_contratacion')
    def validate_fecha_contratacion(cls, value):
        if isinstance(value, str):
            return date.fromisoformat(value)
        return value


class EmployeeUpdate(BaseModel):
    name: str
    email: str
    ciudad: str
    cargo: str
    edad: int
    fecha_contratacion: date
    salario: float
    telefono: str
    direccion: str
    genero: str

    @validator('fecha_contratacion')
    def validate_fecha_contratacion(cls, value):
        if isinstance(value, str):
            return date.fromisoformat(value)
        return value


class EmployeeDelete(BaseModel):
    employee_id: int
