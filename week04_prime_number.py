# week04 prime_number v1.1
# add is_prime function
# Bo Gyung Kim

def is_prime(n) -> bool:
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


start_no, end_no = map(int, input("Enter starting number and ending number : ").split())

if start_no > end_no :
    for k in range(end_no, start_no+1):
        if is_prime(k):
            print(k, end=' ')

else:
    for k in range(start_no, end_no+1):
        if is_prime(k):
            print(k, end=' ')
