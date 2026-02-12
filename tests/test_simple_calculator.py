import pytest
from calculator import SimpleCalculator


def test_instantiation():
    calc = SimpleCalculator()
    assert isinstance(calc, SimpleCalculator)


def test_fsum():
    calc = SimpleCalculator()
    assert calc.fsum(2, 3) == 5
    assert isinstance(calc.fsum(2, 3), int)
    assert calc.fsum(True, 1) == 2


def test_substract():
    calc = SimpleCalculator()
    assert calc.substract(10, 4) == 6
    assert isinstance(calc.substract(10, 4), int)


def test_multiply():
    calc = SimpleCalculator()
    assert calc.multiply(3, 4) == 12
    assert isinstance(calc.multiply(3, 4), int)


def test_divide():
    calc = SimpleCalculator()
    result = calc.divide(10, 2)
    assert result == 5.0
    assert isinstance(result, float)

    assert calc.divide(0, 5) == 0.0


def test_divide_by_zero():
    calc = SimpleCalculator()
    with pytest.raises(ZeroDivisionError):
        calc.divide(10, 0)


def test_invalid_types():
    calc = SimpleCalculator()
    methods = [calc.fsum, calc.substract, calc.multiply, calc.divide]

    for method in methods:
        with pytest.raises(TypeError):
            method(2.5, 3)
        with pytest.raises(TypeError):
            method(2, "3")
        with pytest.raises(TypeError):
            method(None, 3)
