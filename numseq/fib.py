def fib(n):
    a, b = 0, 1
    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        total = 0
        for _ in range(n-1):
            total = a + b
            a, b = b, total
        return total
