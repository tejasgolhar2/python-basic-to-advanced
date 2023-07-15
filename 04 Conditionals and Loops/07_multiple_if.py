"""
In multiple if conditional,
        Whatever be the number of the if conditions, all will be executed
"""
print("Welcome to the Personality Calculator Program !")

hear = input("Do you hear the speaker until his talk finishes completely? Y/N \n")
speak = input(
    "Do you have control on your word flow and language during speaking ? Y/N \n"
)
hygiene = input("Do you spend time in maintaing your body hygiene ? Y/N \n")
addictions = input("Are you addicted to any kind of drugs or addiction ? Y/N \n")

if hear == "Y":
    print("You are a Good Listener")

if speak == "Y":
    print("You are a good speaker")

if hygiene == "Y":
    print("Great ! You are a good person with a fresh feel calm")

if addictions == "N":
    print(
        "It tells how responsible you are towards yours as well as others safety in all aspects"
    )
