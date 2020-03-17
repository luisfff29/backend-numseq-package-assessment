def fib(n):
    if n < 2:
        return n
    else:
        a, b = 0, 1
        total = 0
        for _ in range(n-1):
            total = a + b
            a, b = b, total
        return total
