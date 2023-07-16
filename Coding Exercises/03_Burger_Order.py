"""
Write a program that calculates final bill Burger Order Price based on a user's choice.

Price List.
Mini Burger (M) : $5
Normal Burger (N): $8
Large Burger (L) : $10
Add Mushroom : For Mini and Normal = $1, For Large = $2
Extra Cheese : $1

"""
# TODO
print("Welcome to Burger Shop!")
size = input("What size Burger do you want? M, N or L ")
add_mushroom = input("Do you want mushroom? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
"""
#Approach 1

if size=='M':
    bill = 5
    if add_mushroom=='Y':
        bill += 1
        if extra_cheese=='Y':
            bill += 1
    print(f"Your final bill is: ${bill}.")

if size=='N':
    bill = 8
    if add_mushroom=='Y':
        bill += 1
        if extra_cheese=='Y':
            bill += 1
    print(f"Your final bill is: ${bill}.")
    
if size=='L':
    bill = 10
    if add_mushroom=='Y':
        bill += 2
        if extra_cheese=='Y':
            bill += 1
    print(f"Your final bill is: ${bill}.")
"""

# Approach 2

bill = 0
if size == "M":
    bill += 5

elif size == "N":
    bill += 8

else:  # size=='L'
    bill += 10

if add_mushroom == "Y":
    if size == "L":
        bill += 2
    else:
        bill += 1

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is ${bill}.")
