fruits1 = {"apple","orange","grape","lemon"}


# Method 1 : Use of clear method

# It removes all elements from the set
# After using it, set becomes empty
print(fruits1)

fruits1.clear()
print(fruits1)
# An empty set in python is shown by the set() function and not the curly braces


# Method 2 : Remove Method
# If element to be removed not present in the set, it throws KeyError
# We should be prepared for exception handling

fruits2 = {"apple","orange","grape","lemon"}
print(fruits2)

fruits2.remove("lemon")
print(fruits2)

# fruits2.remove("blackberry")
# print(fruits2)
# it results -->> KeyError: 'blackberry'


# Method 3 : Discard Method
# If the element to be discarded is not present in the set, it doesn't throw any error
# Error Doesn't Occur -->> Difference from the remove() method

fruits3 = {"apple","orange","grape","lemon"}
print(fruits3)

# discard element present in the set
fruits3.discard("apple")
print(fruits3)

# try discarding element not present in the set
fruits3.discard("strawberry")
print(fruits3)


# Method 4: POP method
# A random element from the set is removed
# Cant use the method of Empty-set, It throws error

fruits4 = {"apple","orange","grape","lemon"}
print(fruits4)

fruits4.pop()
print(fruits4)