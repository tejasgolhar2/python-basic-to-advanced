import random
import math

lower = int(input("Enter Lower bound: "))
upper = int(input("Enter Upper bound: "))
num_of_chances =  int(math.log(upper - lower + 1,2))
generated_number = random.randint(lower,upper)
print(f"\n\tYou've only {num_of_chances} chances to guess the integer!\n")
count = 0
flag = False
while count<num_of_chances:
    count+=1
    guess = int(input("Guess a number: "))
    if guess == generated_number:
        flag = True
        print("Congratulations you did it in 3 try\n")
        print(f"The numbers is {generated_number}")
        print("\tBetter Luck Next Time")
        quit()
    elif (guess > generated_number):
        print("You Guessed too high!")
    elif (guess < generated_number):
        print("You Guessed too small!")
if (flag==False):
    print(f"\nThe number is {generated_number}")
print("\tBetter Luck Next Time")
    





# def guessNumber(chances,number,count):
#     while chances
    
#     if (guess > val)and(c<=2) :
#         print("You Guessed too high!")
#         c+=1
#         guessNumber(val,c)
        
#     if (guess < val)and(c<=2):
#         print("You Guessed too small!")
#         c+=1
#         guessNumber(val,c)
#     else:
#         print(f"The numbe is {val}")
#         print("\tBetter Luck Next Time")