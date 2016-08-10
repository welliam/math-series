def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = a+b, a
    return a

def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)
