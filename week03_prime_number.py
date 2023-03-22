# week03_prime_number quiz
start_no = int(input("Enter starting number : "))
end_no = int(input("Enter ending number : "))
is_prime = True

for k in range(start_no, end_no+1):
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


