#   CONVERSION OF LISTS INTO STRINGS

# here we use list function that converts the characters in the string as the individual elements of the string
# the list elements then can be accessed by indexing

# case 1
# each character as the element
custom_string = "tejas"
custom_list = list(custom_string)
print(custom_list)

# case 2
# each word as the element [ USE OF SPLIT METHOD IN PYTHON LISTS ]
# the split method is used to convert the string into list with set of characters separated by space separator
# no need to specify the keyword "list" before the split operator

# Ex1
string1 = "You are a good boy"
list1 = string1.split(" ")
print(list1)

# Ex2
string2 = "You_are_a_bad_boy"
list2 = string2.split("_")
print(list2)



# ACCESSING ELEMENTS OF LIST FORMED USING INDEXING METHOD

print(list2[3])