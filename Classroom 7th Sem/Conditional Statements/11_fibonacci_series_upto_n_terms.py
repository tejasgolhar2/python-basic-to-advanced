n = int(input("Enter the number of terms in fibonacci sequence: "))
fib = 2
while(n!=0):
    if n==1:
        print (fib+1)
    if n>1:
        fib = (fib-1)+(fib-2)
        print(fib)
    n-=1