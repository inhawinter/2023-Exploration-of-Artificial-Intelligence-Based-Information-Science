import primenumber as pn

start_no, end_no = map(int, input("Enter starting number and ending number : ").split())

if start_no > end_no :
    for k in range(end_no, start_no+1):
        if pn.is_prime(k):
            print(k, end=' ')

else:
    for k in range(start_no, end_no+1):
        if pn.is_prime(k):
            print(k, end=' ')
