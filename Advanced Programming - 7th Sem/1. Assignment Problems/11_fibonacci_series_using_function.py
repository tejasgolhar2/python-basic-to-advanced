# 11. Write a program to generate a Fibonacci series using function.

def fibonacci(val):
    a = 0
    b = 1
    if val <= 0:
        print("Please enter a valid term number")
    elif val == 1:
        print(0)
    else:
        print(a)
        print(b)
        while(val>2):
            fibon = a+b
            print(fibon)
            a = b
            b = fibon
            val-=1

num = int(input("Enter the number of terms to be obtained in fibonacci sequence: "))
fibonacci(num)