from datetime import datetime
from typing import List

from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Datos de conexión a la base de datos
db_config = {
    "user": "root",
    "password": "",
    "host": "localhost",
    "port": "3306",
    "database": "users"
}

# Crear la URL de conexión
db_url = f"mysql+pymysql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}"

# Crear el motor de la base de datos
engine = create_engine(db_url)

# Crear la sesión de la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Crear la tabla de usuarios
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    email = Column(String(50), unique=True)
    created_at = Column(DateTime, default=datetime.now)


# Crear la tabla en la base de datos
Base.metadata.create_all(bind=engine)


# Crear la clase de modelo de usuario
class UserIn(BaseModel):
    name: str
    email: str


# Crear la clase de modelo de usuario con su id
class UserOut(UserIn):
    id: int


# Crear la clase de modelo de lista de usuarios
class UsersOut(BaseModel):
    users: List[UserOut]


# Crear la aplicación FastAPI
app = FastAPI()


# Ruta de prueba
@app.get("/")
def read_root():
    return "Bienvenidos a mi api"


# Crear un nuevo usuario
@app.post("/users/")
def create_user(user: UserIn):
    db = SessionLocal()
    db_user = User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return UserOut(id=db_user.id, name=db_user.name, email=db_user.email)


# Obtener una lista de todos los usuarios
@app.get("/users/", response_model=UsersOut)
def read_users():
    db = SessionLocal()
    users = db.query(User).all()
    return UsersOut(users=[UserOut(id=user.id, name=user.name, email=user.email) for user in users])


@app.put("/users/{user_id}")
def update_user(user_id: int, user: UserIn):
    db = SessionLocal()
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db_user.name = user.name
        db_user.email = user.email
        db.commit()
        db.refresh(db_user)
        return UserOut(id=db_user.id, name=db_user.name, email=db_user.email)
    else:
        return {"message": f"User with id {user_id} not found"}


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    db = SessionLocal()
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return {"message": f"User with id {user_id} deleted successfully"}
    else:
        return {"message": f"User with id {user_id} not found"}


@app.get("/users/{user_id}", response_model=UserOut)
def read_user(user_id: int):
    db = SessionLocal()
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        return UserOut(id=db_user.id, name=db_user.name, email=db_user.email)
    else:
        return {"message": f"User with id {user_id} not found"}
