# week06_function.py
# after decorator
import time

def time_checker(func):
    def inner(*args):
        s = time.time()
        r = func(*args)
        e = time.time()
        print(f'총 수행시간은 {e-s}초 입니다')
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
#@time_checker
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


print(power(2,10))
df = time_checker(factorial)
help(power)
help(factorial)
print(df(1000))
dp = time_checker(power)
print(dp(2, 100000))

def factorial_recursion(n):
    """
    factorial function with recursion
    :param n: >0
    :return: n!
    """
    if n == 1:
        return 1
    else:
        return n * factorial_recursion(n-1)

def fibonacci_recursion(n):
    """
    fibonacci number function
    :param n: integer value
    :return: fibonacci number
    """
    if n <= 1:
        return n
    else:
        return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)


if __name__ == "__main__":
    number = int(input("정수 입력 : "))
    print(factorial_recursion(number))
    print(factorial(number))
    print(fibonacci_recursion(number))
    print(fibonacci(number))

