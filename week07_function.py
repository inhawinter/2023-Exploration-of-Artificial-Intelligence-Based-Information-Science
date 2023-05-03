import my_util


#@my_util.time_checker
def factorial_repetition(n):
    """
    factorial function with repetition
    :param n: > 0
    :return: n!
    """
    result = 1
    for k in range(1, n+1):
        result = result * k
    return result


#@my_util.time_checker
def factorial_recursion(n):
    """
    factorial function with recursion
    :param n: > 0
    :return: n!
    """
    if n == 1:
        return 1
    else:
        return n * factorial_recursion(n-1)



memo = [None for _ in range(100)]

"""
    }else{
        // 0이라는 것은 아직 계산이 된적이 없다는 것...
        // 계산을 하고 저장해둔다.
        // 그리고 값을 반환한다.
        data[x] = fibonacci(x-1) + fibonacci(x-2);
        return data[x];
    }
"""
#@my_util.time_checker
def fibonacci_recursion(n):
    """
    fibonacci number function
    :param n: integer value
    :return: fibonacci number
    """
    if n <= 1:
        return n
    if memo[n] is not None:
        return memo[n]
    else:
        memo[n] = fibonacci_recursion(n-1) + fibonacci_recursion(n-2)
        return memo[n]


if __name__ == "__main__":
    number = int(input("정수 입력 : "))
    print(factorial_recursion(number))
    print(factorial_repetition(number))
    print(fibonacci_recursion(number))
