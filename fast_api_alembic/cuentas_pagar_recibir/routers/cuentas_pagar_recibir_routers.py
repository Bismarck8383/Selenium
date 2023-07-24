from fastapi import APIRouter
from pydantic import BaseModel
from decimal import Decimal

router = APIRouter(prefix="/cuentas_pagar_recibir")


class CuentaPagaRecibirResponse(BaseModel):
    id: int
    descripcion: str
    valor: Decimal
    tipo: str  # pagar o recibir


@router.get("/")
def lista_cuentas():
    return [
        CuentaPagaRecibirResponse(
            id=1,
            descripcion="Alquiler",
            valor=Decimal("450.0"),
            tipo="Pagar"
        ),
        CuentaPagaRecibirResponse(
            id=2,
            descripcion="Salario",
            valor=Decimal("1225.00"),
            tipo="Recibir"
        )
    ]

