import random
names = input("Input everyone's name, separated by a comma. ")
list1 = names.split(", ")
name = random.choice(list1)
print(name,"is going to pay for the meal today!")