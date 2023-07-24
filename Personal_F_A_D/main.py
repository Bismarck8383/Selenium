from fastapi import FastAPI
from starlette.responses import HTMLResponse
from router import router
from uvicorn import run

app = FastAPI()

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


if __name__ == "__main__":
    # run("main:app", reload=True)
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8007, reload=True)
# uvicorn main:app --reload
