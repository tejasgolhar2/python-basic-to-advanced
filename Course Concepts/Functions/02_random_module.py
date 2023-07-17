'''
        The random module in Python is a built-in module that provides functions 
    for generating random numbers, selecting random elements from a sequence, 
    shuffling sequences, and more. 
        It is commonly used for tasks that require randomness or unpredictability. 
        This module finds its prime application in places where randomness is important
    like games, test cases, etc.
'''
import random

# the below function will help to give a random value between the entered range
print("Random integer in the given range - ")
peak = int(input("Enter the maximum value of the range: "))
num = random.randint(1,peak)
print(f"Random value: {num}")

