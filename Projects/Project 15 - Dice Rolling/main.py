import random

def rollDice():
    print(f"Dice1: {random.randint(1,6)}")
    print(f"Dice2: {random.randint(1,6)}")
    ask = input("Roll the dice again? (Y/N)")
    if ask=="Y":
        rollDice()
    else:
        quit()


rollDice()