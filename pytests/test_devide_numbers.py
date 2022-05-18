import pytest

from divide_numbers import div, inc

def test_div():
    assert 5 == div(10, 2)


def test_divide_by_zero_error():
    with pytest.raises(ZeroDivisionError) as excinfo:
        div(10, 0)
    assert "division by zero" in str(excinfo.value)


@pytest.mark.parametrize("test_input, expected", [(1,2), (2,3), (3,4)])
def test_inc(test_input, expected):
    assert expected == inc(test_input)