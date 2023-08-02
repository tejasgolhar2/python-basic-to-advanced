import random

def play_again():
    choose = ["rock","paper","scissors"]
    user_choice = input("Enter a choice (rock, paper, scissors): ")
    comp_choice = random.choice(choose)
    print(f"\nYou chose {user_choice}, computer chose {comp_choice}")
    choice(user_choice,comp_choice)

def ask_to_play():
    ask = input("Play again (Y/N)? ")
    if ask == "Y":
        play_again()
    else:
        quit()

def choice(user_choice, comp_choice):
    if user_choice=="paper":
        if comp_choice=="rock":
            print("\nPaper covers rock! You won.")
        if comp_choice=="scissors":
            print("\nScissors cuts paper! You lose.")
        if comp_choice=="paper":
            print("\nBoth are same")

    if user_choice=="rock":
        if comp_choice=="rock":
            print("\nBoth are same")
        if comp_choice=="scissors":
            print("\nRock break scissors! You won.")
        if comp_choice=="paper":
            print("\nPaper covers rock! You lose.")

    if user_choice=="scissors":
        if comp_choice=="rock":
            print("\nRock break scissors! You lose")
        if comp_choice=="scissors":
            print("\n\nBoth are same")
        if comp_choice=="paper":
            print("\nScissors cuts paper! You won.")
    ask_to_play()

choose = ["rock","paper","scissors"]
user_choice = input("Enter a choice (rock, paper, scissors): ")
comp_choice = random.choice(choose)
print(f"\nYou chose {user_choice}, computer chose {comp_choice}")
choice(user_choice,comp_choice)




