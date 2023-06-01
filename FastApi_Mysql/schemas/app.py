from fastapi import FastAPI

from FastApi_Mysql.routes.user import user

app = FastAPI()

app.include_router(user)
