def square(n):
    """
    Returns the nth term of the numbers that can
    be arranged into square geometric shapes
    """
    return n**2


def triangle(n):
    """
    Returns the nth term of the numbers that can
    be arranged in triangular geometric shapes
    """
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
    """
    Returns the nth term of the numbers that
    can be arranged as symmetric cube shapes
    """
    return n*n*n
