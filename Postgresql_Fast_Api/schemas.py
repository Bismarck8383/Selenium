from __future__ import annotations
from typing import List, Optional
from pydantic import BaseModel
from datetime import date


class BookBase(BaseModel):
    titulo: str
    autor: str
    descripcion: Optional[str] = None


class BookCreate(BookBase):
    pass


class LoanOut(BaseModel):
    id: int
    libro_id: int
    usuario_id: int
    fecha_prestamo: date
    fecha_devolucion: Optional[date] = None

    class Config:
        orm_mode = True


class Book(BookBase):
    id: Optional[int]  # Haz que el campo id sea opcional
    prestamos: List[LoanOut] = []

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    nombre: str
    apellido: str
    email: str
    telefono: Optional[str] = None


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
    prestamos: List[LoanOut] = []

    class Config:
        orm_mode = True


class LoanBase(BaseModel):
    libro_id: int
    usuario_id: int
    fecha_prestamo: date
    fecha_devolucion: Optional[date] = None


class LoanCreate(LoanBase):
    pass


class Loan(LoanBase):
    id: int

    class Config:
        orm_mode = True
