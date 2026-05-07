import pytest
from calculadora import suma, resta, multiplicacion, division

def test_suma():
    assert suma(14, 9) == 23

def test_resta():
    assert resta(25, 7) == 18

def test_multiplicacion():
    assert multiplicacion(6, 8) == 48

def test_division():
    assert division(36, 6) == 6

def test_division_cero():
    with pytest.raises(ValueError):
        division(12, 0)