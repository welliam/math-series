def sum_series(n, a=0, b=1):
    '''Return nth value of Fibonacci-like series, with optional custom
    base cases.'''
    if n == 0:
        return a
    for i in range(n-1):
        a, b = b, a+b
    return b


def fibonacci(n):
    '''Return nth value of Fibonacci sequence.'''
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a


def lucas(n):
    '''Return nth value of Lucas sequence'''
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)
