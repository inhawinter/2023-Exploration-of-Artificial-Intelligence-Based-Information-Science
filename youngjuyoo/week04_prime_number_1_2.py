import primenumber
start_no, end_no = map(int, input("Enter starting number and ending number : ").split())
if start_no > end_no:
   start_no, end_no = end_no, start_no
for k in range(start_no, end_no+1):
    if primenumber.is_prime(k):
        print(k, end=' ')