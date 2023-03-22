# week03 prime_number v0.8
# numbers = input("Enter starting number and ending number : ").split()
# print(numbers)
# start_no = int(numbers[0])
# end_no = int(numbers[1])
start_no, end_no = input("Enter starting number and ending number : ").split()

is_prime = True

for k in range(int(start_no), int(end_no)+1):
    is_prime = True
    if k < 2:
        is_prime = False
    else:
        for i in range(2, k):
            if k % i == 0:
                is_prime = False
                break
        if is_prime:
            print(k, end=' ')
