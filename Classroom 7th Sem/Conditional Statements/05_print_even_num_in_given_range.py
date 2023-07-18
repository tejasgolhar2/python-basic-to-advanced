num = int(input("Enter the range upto which even numbers are to be printed: "))
for n in range(0,num+1):
    if n%2 == 0:
        print(n)