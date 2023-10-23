# Declaring and Defining Set in Python

# Approach 1 : Using syntax

#     A set can be initialised by using curly braces
#    Python dictionaries also being having the curly braces are different from sets that they doesn't contain keys

#    The elements present in the set as objects are Immutable ( can't be modified )


set1 = {'a','b','c',1,2,3}
print(set1)


# Approach 2 : Using set function


# Creating empty set
# We cannot use empty braces only to create an empty set

# Method 1 :  Wrong method
set2 = {}
print(type(set2))

# Method 2 : Using Function
set3 = set()
print(type(set3))

# Method 3 : Using syntax
#   This type of set initialization is not recommeded
new_set = {*""}
print(type(new_set))



# Convert Other datatype objects into set

# List
#   No repetition is allowed in Python Sets.
#       The set elments doesn't have a fixed location in the set i.e., the individual element cannot be directly accessed 
#   by the concept of indexing
list1 = [1,2,2,3,4,5,6,2,5,6,2,5,6,2,5]
print(list1)
set4 = set(list1)
print(set4)


# Tuple 
tuple1 = ("tejas","kunal","Rabina","Prakash")
print(tuple1)
set5 = set(tuple1)
print(set5)


# Dictionary
# Only the dictionary keys are obtained as set items
dict1 = {   1:"One",
            2: "Two",
            3:"Three",
        }
print(dict1)
set6 = set(dict1)
print(set6)