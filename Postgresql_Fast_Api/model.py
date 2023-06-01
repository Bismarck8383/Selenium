from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship

from config import Base


class Book(Base):
    __tablename__ = 'libros'
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(255), index=True)
    autor = Column(String(255), index=True)
    descripcion = Column(String(1000))
    prestamos = relationship("Loan", back_populates="libro")


class User(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255))
    apellido = Column(String(255))
    email = Column(String(255), unique=True, index=True)
    telefono = Column(String(255))
    prestamos = relationship("Loan", back_populates="usuario")


class Loan(Base):
    __tablename__ = 'prestamos'
    id = Column(Integer, primary_key=True, index=True)
    libro_id = Column(Integer, ForeignKey('libros.id'))
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    fecha_prestamo = Column(Date)
    fecha_devolucion = Column(Date)
    libro = relationship("Book", back_populates="prestamos")
    usuario = relationship("User", back_populates="prestamos")
