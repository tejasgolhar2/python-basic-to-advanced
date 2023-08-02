import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = "1234567890"
symbols = "-+=!@#$%^&*"

num_of_letters = int(input("How many letters do you want in your password? "))
num_of_numbers = int(input("How many numbers do you want in your password? "))
num_of_symbols = int(input("How many symbols do you want in your password? "))

val = ""
while num_of_letters:
    if num_of_letters==0:
        break
    val = val+random.choice(letters)
    num_of_letters-=1

while num_of_numbers:
    if num_of_numbers==0:
        break
    val = val+random.choice(nums)
    num_of_numbers-=1

while num_of_symbols:
    if num_of_symbols==0:
        break
    val = val+random.choice(symbols)
    num_of_symbols-=1

print(f"Your password is: {val}")
