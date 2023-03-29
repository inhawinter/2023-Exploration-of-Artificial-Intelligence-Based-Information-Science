# week04 prime_number v1.1
<<<<<<< HEAD
# add is_prime function
# feat youngju
=======

>>>>>>> 8cdf1c845a235c5216a9e75eb3d0f3dae7a49429
def is_prime(n) -> bool:
    """
    Check prime number
    :param n: integeumber
    :return: True (if number is prime number) / False (if number is NOT prime number)
    """
    if k < 2:
        return False
    else:
        for i in range(2, k):
            if k % i == 0:
                return False
    return True

k = 0
start_no, end_no = map(int, input("Enter starting number and ending number : ").split())
<<<<<<< HEAD
if start_no > end_no:
    k=start_no
    start_no = end_no
    end_no = k
=======

if start_no > end_no : start_no, end_no = end_no, start_no

>>>>>>> 8cdf1c845a235c5216a9e75eb3d0f3dae7a49429
for k in range(start_no, end_no+1):
    if is_prime(k):
        print(k, end=' ')