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


def demonstrate_series(f, inputs):
    name = f.__name__
    print('  Returns the nth value in the {} series'
          .format(name.capitalize()))
    print('{}(n):'.format(name))
    for i in inputs:
        print('>>> {}({})'.format(name, i))
        print(f(i))
    print()


def demonstrate_sum_series():
    print('sum_series(n, a=0, b=1):')
    print('  Returns the nth value of a fibonacci-like sequence',
          'with a and b as base cases.')
    print('>>> sum_series(30)')
    print(sum_series(30))
    print('>>> sum_series(15, 2, 1)')
    print(sum_series(15, 2, 1))
    print('>>> sum_series(123, 423, 438053)')
    print(sum_series(123, 423, 438053))


if __name__ == '__main__':
    print('This module defines functions that implement mathematical series.')
    print()
    demonstrate_series(fibonacci, [0, 2, 30])
    demonstrate_series(lucas, [0, 5, 15])
    demonstrate_sum_series()
