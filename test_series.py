import pytest

FIBS_TABLE = [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (30, 832040)
]


@pytest.mark.parametrize('n, result', FIBS_TABLE)
def test_fibonacci(n, result):
    """Test function `fibonacci' outputs correct values for the
    Fibonacci sequence."""
    from series import fibonacci
    assert fibonacci(n) == result
