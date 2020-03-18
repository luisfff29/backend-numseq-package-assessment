def is_prime(m):
    """Returns a boolean indicating whether m is a prime number"""
    if m < 2:
        return False
    elif m == 2:
        return True
    elif m % 2 == 0:
        return False
    else:
        for i in range(3, 1 + int(m**0.5), 2):
            if m % i == 0:
                return False
        return True


def primes(n):
    """Returns a list of all prime numbers less than n"""
    return [num for num in range(n) if is_prime(num)]
