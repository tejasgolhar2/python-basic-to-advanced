'''    8. Write a program to find the factorial of number from given range. 
    For example, find the factorial of all numbers in range from 35 to 75
'''

low = int(input("Enter the lower number in range: "))
high = int(input("Enter the higher number in range: "))

for item in range(low,high+1):
    print("Factorial of {} is : ".format(item))
    fact = 1
    for i in range(1,item+1):
        fact *= i
    print(fact)


