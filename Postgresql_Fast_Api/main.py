from fastapi import FastAPI
from starlette.responses import HTMLResponse

from model import Base
from config import engine
from router import router

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Incluir el router en la aplicación FastAPI
app.include_router(router, prefix="/api")


@app.get('/')
def home():
    html_content = """
       <html>
           <head>
               <title>App Biblioteca</title>
           </head>
           <body>
               <h1>Bienvenido  APP Biblioteca!</h1>
               <p>Aplicación de pureba para Fast Api!</p>
           </body>
       </html>
       """
    return HTMLResponse(content=html_content, status_code=200)

# uvicorn app:app --reload
