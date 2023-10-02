#       To compare the two or more string values, the comparison of 
#   strings can be done using comparison operators likewise used in arithmetic operations


# USE OF EQUAL_TO OPERATOR IN PYTHON STRINGS

def checkPassword():
    password = "strong"
    val = input("Re-enter Password: ")
    if val == password:
        print("Welcome to the system!")
    else:
        checkPassword()

password = "strong"
val = input("Enter Password: ")
if val == password:
    print("Welcome to the system!")
else:
    checkPassword()



# USE OF GREATER THAN OR LESSER THAN OPERATOR IN PYTHON STRINGS

# the comparison is done for the first characters of the strings as per their values in Unicode System
# The Uppercase letters comes before the lowercase letters in Unicode system

name1 = "tejas"
random_name =  input("Enter a string value: ")

if random_name < name1:
    print(f"The random name {random_name} comes before the name {name1}, alphabetically.")
elif random_name > name1:
    print(f"The random name {random_name} comes after the name {name1}, alphabetically.")


# USE OF ASSGNMENT OPERATOR IN STRINGS

# print("Lets try to modify the name1 variable: ")
# name1[0] = "n"
# print(name1)

# Error Here : TypeError: 'str' object does not support item assignment



# ALTERNATIVE WAY TO CHANGE THE CHARACTER IN STRING

#     Just create a new variable and use the  proper python formatting 
#   methods to change the intended character of the string variable

# adding the first updated character
name2 = "N" + name1[1:]
print(name2)

# update characters in the middle of the string
name3 = name1[0:3] + "vir" + name1[3:]
print(name3)