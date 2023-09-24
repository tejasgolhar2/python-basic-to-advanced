# Traversal through a Dictionary

list1 = { 1:'one',2:'two',3:'three',4:'four'}


# Printing a dictionary 
print(list1)

# Looping through a dictionary
for item in list1:
    print(item,':',list1[item])

# Using items() method to loop through dictionary values
for item,value in list1.items():
    print(item,value)