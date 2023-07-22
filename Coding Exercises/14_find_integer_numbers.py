# Implement a program which finds integer numbers from given List.

# Input
# custom_list = [11, 30.1, 90.2, 30, 45.1, 54, '54']

custom_list = [11, 30.1, 90.2, 30, 45.1, 54, "54"]

for number in custom_list:
    if isinstance(number, int) == True:
        print(number)

#       The isinstance is a builtin function which take two arguments
#   ( one object and the other object type to be checked) and compares the object
#   whether is of the mentioned type or not and returns the truth value
