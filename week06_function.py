# week06_function.py
# before decorator
import time

def factorial(n):
    """
    factorial function
    :param n: more than zero
    :return: n!
    """
    s = time.time()
    result = 1
    for k in range(1, n+1):
        result = result * k
    e = time.time()
    print(f'총 수행시간은 {e-s}초 입니다')
    return result


def power(b, e):
    """
    power function
    :param b: base, ex) 2
    :param e: exponent, ex) 10
    :return: ex) 2 to the 10th power is 1024.
    """
    s = time.time()
    result = 1
    for _ in range(e):
        result = result * b
    e = time.time()
    print(f'총 수행시간은 {e-s}초 입니다')
    return result


print(power(2, 10))
print(factorial(1000))

