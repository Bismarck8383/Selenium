import time

import pytest


@pytest.fixture(scope='module')
def setup_login():
    print("empezando")
    yield
    print("\nsiguiendo")
    print("corriendo")


def test_uno(setup_login):
    print("vamos...........")
