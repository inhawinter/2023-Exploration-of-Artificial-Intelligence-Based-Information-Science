# week04 prime_number v1.0
# add is_prime function
# modified by minjae Kim

def is_prime(n) -> bool:
    """
    Check prime number
    :param n: integer number
    :return: True (if number is prime number) / False (if number is NOT prime number)
    """
    if k < 2:
        return False
    else:
        for i in range(2, k):
            if k % i == 0:
                return False
    return True


numbers = sorted(map(int, input("Enter starting number and ending number : ").split()))

for k in range(numbers[0], numbers[1] + 1):
    if is_prime(k):
        print(k, end=' ')
