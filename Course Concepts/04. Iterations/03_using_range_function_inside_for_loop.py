# Write a Python Program to print sum number from 1 to n

sum = 0
n = int(input("Enter the highest number to get the sum: "))
for number in range(n):
    sum += number
print(sum)