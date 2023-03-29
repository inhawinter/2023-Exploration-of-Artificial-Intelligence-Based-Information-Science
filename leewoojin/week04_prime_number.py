# week04 prime_number v1.0
# add is_prime function
# Lee woojin

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
            if n % i == 0:
                return False
    return True


def reversable_prime_print(low_num, high_num):

    # swap lowNum & highNum
    if low_num > high_num:
        temp_num = low_num
        low_num = high_num
        high_num = temp_num

    # printing primes
    for k in range(low_num, high_num + 1):
        if is_prime(k):
            print(k, end=' ')

    
start_no, end_no = map(int, input("Enter starting number and ending number : ").split())

reversable_prime_print(start_no, end_no)