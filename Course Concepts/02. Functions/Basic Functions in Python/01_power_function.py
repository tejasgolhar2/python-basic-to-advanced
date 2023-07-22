print("Welcome to Power Calculator Program")

"""
#Approach 1: 

base = float(input("Enter the base value: "))
index = float(input("Enter the exponent value: "))
val = 1
while index!=0:
    val = val * base
    index = index-1

if index == 0:
    print(f"The value of power is {val}")

"""

#Approach 2: 

import math

base = float(input("Enter the base value: "))
index = float(input("Enter the exponent value: "))

val = pow(base, index)

print(f"The value of power is {val}")
