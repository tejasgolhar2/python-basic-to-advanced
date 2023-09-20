# Traversal through a Dictionary

list1 = { 1:'one',2:'two',3:'three',4:'four'}

# Printing a dictionary 
print(list1)

# Looping through a dictionary
# this will print all the keys in the dictionary and not the values
for item in list1:
    print(item)

# this is rather a complex way of iterating through a dictionary
for item in list1:
    print(item,':',list1[item])