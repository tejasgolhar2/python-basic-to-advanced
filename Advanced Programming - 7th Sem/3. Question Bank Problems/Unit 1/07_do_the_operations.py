# Write a Program to perform following operations:
# a. Find max among two numbers.
# b. Find sum of all list element.


ch = int(input("Choose the operation: \n1. Find max among two numbers\n2.Find sum of all list elements\n"))

if ch==1:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    ans = max(num1,num2)

    print(f"The maximum among {num1} and {num2} is {ans}")

elif ch==2:
    size = int(input("Enter the size of the list: "))
    list1 = []
    sum = 0
    for i in range(size):
        list1.append(int(input("Enter list element: ")))
        sum += list1[i]
    
    print("Sum of list elements: ",sum)
    
