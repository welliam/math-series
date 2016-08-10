import pytest

FIBS_TABLE = [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (30, 832040)
]

LUCAS_TABLE = [
    (0, 2),
    (1, 1),
    (2, 3),
    (3, 4),
    (7, 29),
]


@pytest.mark.parametrize('n, result', FIBS_TABLE)
def test_fibonacci(n, result):
    """Test function `fibonacci' outputs correct values for the
    Fibonacci sequence."""
    from series import fibonacci
    assert fibonacci(n) == result


@pytest.mark.parametrize('n, result', LUCAS_TABLE)
def test_lucas(n, result):
    """Test function `lucas' outputs correct values for the Lucas
    sequence."""
    from series import lucas
    assert lucas(n) == result


@pytest.mark.parametrize('n, result', FIBS_TABLE)
def test_sum_series(n, result):
    """Test function `sum_series' outputs correct values for the
    Fibonacci sequence (i.e., the case where optional parameters are
    not supplied)."""
    from series import sum_series
    assert sum_series(n) == result


@pytest.mark.parametrize('n, result', LUCAS_TABLE)
def test_sum_series(n, result):
    """Test function `sum_series' outputs correct values for the
    Lucas sequence."""
    from series import sum_series
    assert sum_series(n, 2, 1) == result
