# Tuples
#     It is a datatype in Python. It is represented just as in lists.
# Tuples are represented by round brackets.
# The individual items in the tuples can be accessed by indexing.
# The only difference is that tuples are immutable.

# While declaring the tuples, we can either use parentheses or can write the elements as they are.  
# The parentheses in tuples are optional.

# Creating a Tuple
# Approach 1
my_tuple1 = (1,2,3,4)
print(my_tuple1)

# Approach 2
my_tuple2 = 1,2,3,4
print(my_tuple2)


# When theres a single element in tuple
# Wrong Approach
tuple3 = (1)
print(tuple3)
print(type(tuple3))

# COrrect Approach
tuple4 = (1,)
print(tuple4)
print(type(tuple4))


# When tried printing tuple directly using Print function
print(1,2,3,4)
# This will print each value separated by comma as an individual variable

print((1,2,3,4))
# This will print the tuple containg the elements as mentioned 


# To create an empty tuple
# Approach 1 : Using Syntax
tuple5 = ()
print(tuple5)

# Approach 2 : Using Builtin function
tuple6 = tuple()
print(tuple6)

# COverting  A STRING and A LIST INTO TUPLE
tuple7 = tuple("Krishn")
print(tuple7)

tuple8 = tuple([1,2,3,4,5])
print(tuple8)