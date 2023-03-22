# week03_prime_number v0.6
number = int(input("Input number : "))
is_prime = True

if number < 2:
    is_prime = False
else:
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

if is_prime:
    print(f'{number} is prime number!')
else:
    print(f'{number} is NOT prime number.')
