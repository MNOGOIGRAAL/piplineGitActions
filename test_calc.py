from calc import addition
from calc import subtraction


def test_addition():
    result = addition(5, 5)
    assert result == 10

def test_subtraction():
    result = subtraction(7, 2)
    assert result == 5