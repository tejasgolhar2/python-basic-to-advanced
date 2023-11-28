# Write a Program to print first 10 Prime Numbers
import math

def printPrime(num):
    for number in range(2,num):
        flag = False

        for i in range(2,number):
            if number%i==0:
                flag = True
                break
            num-=1

        if not flag:
            print(number)
            
num = int(input("Enter the number of prime numbers to be printed: "))
printPrime(num)