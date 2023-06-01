import time

import pytest
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

benchmark_settings = {
    "min_time": 0.1,
    "max_time": 0.5,
    "min_rounds": 5,
    "timer": time.time,
    "disable_gc": True,
    "warmup": False
}


@pytest.mark.benchmark(group="books", **benchmark_settings)
def test_create_new_book(benchmark):
    def create_book():
        for i in range(100):
            new_book = {
                "titulo": f"Libro de prueba {i}",
                "autor": f"Autor de prueba {i}",
                "descripcion": f"Descripción del libro de prueba {i}"
            }
            response = client.post("/api/books", json=new_book)
            assert response.status_code == 200, f"Error al crear el libro de prueba {i}"

    benchmark(create_book)
    return time.sleep(0.000001)


@pytest.mark.benchmark(
    group="books",
    min_time=0.1,
    max_time=0.5,
    min_rounds=5,
    timer=time.time,
    disable_gc=True,
    warmup=False
)
def test_get_all_books_list(benchmark):
    response = client.get("/api/books")
    assert response.status_code == 200, "Error no obtiene los libros"
    benchmark(response.json)
    return time.sleep(0.000001)


@pytest.mark.benchmark(
    group='loans',
    min_time=0.1,
    max_time=0.5,
    min_rounds=5,
    timer=time.time,
    disable_gc=True,
    warmup=False
)
def test_get_all_loans_list(benchmark):
    response = client.get("/api/loans")
    estado = response.status_code
    # Verifica que la respuesta tenga un código de estado 200 OK
    assert response.status_code == 200, f"Error: no se pudo obtener la lista de préstamos, respuesta {estado}"
    # Verifica que la respuesta tenga una lista de préstamos en formato JSON
    assert isinstance(response.json(), list), "Error: la respuesta no contiene una lista de préstamos en formato JSON"

    # Verifica que la respuesta tenga al menos un préstamo en la lista
    assert len(response.json()) > 0, "Error: la lista de préstamos está vacía"

    # Verifica que cada préstamo en la lista tenga los campos esperados
    for loan in response.json():
        assert "id" in loan, "Error: el préstamo no tiene el campo 'id'"
        assert "libro_id" in loan, "Error: el préstamo no tiene el campo 'libro_id'"
        assert "usuario_id" in loan, "Error: el préstamo no tiene el campo 'usuario_id'"
    benchmark(response.json)


@pytest.mark.benchmark(
    group='users',
    min_time=0.1,
    max_time=0.5,
    min_rounds=5,
    timer=time.time,
    disable_gc=True,
    warmup=False
)
def test_get_all_users_list(benchmark):
    benchmark.extra_info['foo'] = 'bar'

    response = client.get("/api/users")
    assert response.status_code == 200, "Error no obtiene los usuarios"
    benchmark(response.json)


@pytest.mark.benchmark(
    group='/vista_prestamos',
    min_time=0.1,
    max_time=0.5,
    min_rounds=5,
    timer=time.time,
    disable_gc=True,
    warmup=False
)
def test_get_vista_prestamos(benchmark):
    benchmark.extra_info['foo'] = 'bar'

    response = client.get("/api/vista_prestamos")
    assert response.status_code == 200, "Error no se obtuvo la vista"
    benchmark(response.json)

# para ejecutar mi codigo en consola
# pytest --benchmark-autosave --benchmark-save=testpytest --benchmark-json=informe.json
