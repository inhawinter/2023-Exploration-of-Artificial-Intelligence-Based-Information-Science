# week06_function.py
# after decorator
import time


def time_checker(func):  # closure
    def inner(*args):
        s = time.time()
        r = func(*args)
        e = time.time()
        print(f'총 수행시간은 {e - s}초 입니다')
        return r
    return inner


def factorial(n):
    """
    factorial function
    :param n: more than zero
    :return: n!
    """
    result = 1
    for k in range(1, n+1):
        result = result * k
    return result


@time_checker
def power(b, e):
    """
    power function
    :param b: base, ex) 2
    :param e: exponent, ex) 10
    :return: ex) 2 to the 10th power is 1024.
    """
    result = 1
    for _ in range(e):
        result = result * b
    return result



print(power(2, 10))

df = time_checker(factorial)
print(df(1000))



