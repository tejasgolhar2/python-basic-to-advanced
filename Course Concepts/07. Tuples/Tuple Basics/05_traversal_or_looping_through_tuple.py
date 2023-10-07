# TRAVERSAL THROUGH A TUPLE -- Visiting every element of a tuple at least once


new_tuple = ( 1,2,3,4,5)

# Printing every value of the tuple

for value in new_tuple:
    print(value)


# Printing index for every value in TUple

# Approach 1
# Here, we need to update the value of index after every loop cycle
index = 0
for value in new_tuple:
    print(index,"-",value)
    index+=1

# Approach 2
# Using the range function
# Here, we need to update the value indexing to obtain the elements right from 1st index

for item in range(len(new_tuple)):
    val = new_tuple[item]
    print(item,"-",val)

# Approach 3 
# Using Enumerate function
# It returns tuple
# It works using the concept of Tuple Unpacking 

# For Tuple
for index,value in enumerate(new_tuple):
    print(index,"-",value)

# For list
list1 = ["one","two","three"]

for index,item in enumerate(list1):
    print(index,"-",item)


# Strating index of Tuple in Enumeration

# the starting index from enumerate function can be controlled
# It's a temporary change lies till the scope of the loop and not permanent

for index,value in enumerate(new_tuple,2):
    print(index,"-",value)