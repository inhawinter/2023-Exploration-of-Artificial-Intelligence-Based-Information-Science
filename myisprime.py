def is_prime(a,b) -> bool:
    """
    Check prime number
    :param n: integer number
    :return: True (if number is prime number) / False (if number is NOT prime number)
    """
    if n < 2:
        return False
    else:
        for i in range(2, n):
            if k % i == 0:
                return False
    return True
