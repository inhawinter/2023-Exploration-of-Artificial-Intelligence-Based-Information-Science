# week03_prime_number v0.5
number = int(input("Input number : "))
is_prime = True

for i in range(2, number):
    if number % i == 0:
        is_prime = False
        break  # If not prime number, exit the loop as soon as the first divisor is found.
    print(i, end=' ')

#if is_prime == True:
if is_prime:  # remove comparison
    print(f'{number} is prime number!')
else:
    print(f'{number} is NOT prime number.')
