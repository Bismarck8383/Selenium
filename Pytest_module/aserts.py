import pytest


@pytest.mark.validar
def test_validar():
    name1 = "pepelote"
    name2 = "pepe"

    assert name2 == name1, "no Son iguales"
