def square(n):
    return n**2


def triangle(n):
    if n > 1:
        constant = 2
        result = 1
        for _ in range(n-1):
            result = result + constant
            constant += 1
        return result
    else:
        return n


def cube(n):
    return n*n*n
