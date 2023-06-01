from fastapi import APIRouter

from FastApi_Mysql.conec.db import conn
from FastApi_Mysql.models.user import users

user = APIRouter()


@user.get('/')
def index():
    return "Bienvenido"


@user.get("/users")
def get_users():
    return conn.execute(users.select().fetch_all())
