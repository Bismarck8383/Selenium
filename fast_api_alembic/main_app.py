import uvicorn
from fastapi import FastAPI

from cuentas_pagar_recibir.routers import cuentas_pagar_recibir_routers


app = FastAPI()


@app.get("/")
def deeveloper() -> str:
    return "Yo soy Bismarck"


app.include_router(cuentas_pagar_recibir_routers.router)


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8002)
