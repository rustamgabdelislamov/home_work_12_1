from decorators.log import log
import pytest


@log("log.txt")
def div(a, b):
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b


def test_b_not_zero():
    assert div(2, 1) == 2.0


def test_b_zero():
    with pytest.raises(ZeroDivisionError):
        div(2, 0)


# def test_b_not_zero_(capsys):
#     result = div(2,1)
#
#     assert result == 2.0
#
#     captured = capsys.readouterr()
#     assert "div ok" in captured.out
#
#
# def test_b_zero_(capsys):
#     with pytest.raises(ZeroDivisionError) as excinfo:
#         div(2, 0)
#
#     assert str(excinfo.value) == "division by zero"
#
#     # Проверяем, что логирование произошло
#     captured = capsys.readouterr()
#     assert "div error: division by zero. Inputs: 2, 0" in captured.out
