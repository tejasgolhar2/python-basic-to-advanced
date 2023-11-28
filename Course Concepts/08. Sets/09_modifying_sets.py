# The union doesn't result in modification in original sets

fruits1 = {"apple", "pear", "limon", "grape", "cucumber", "orange"}
vegetables1 = {"cucumber", "garlic", "onion", "broccoli", "pepper"}

union_set1 = fruits1 | vegetables1

print(union_set1)

print(fruits1)              # No modification
print(vegetables1)


# Modify the Original Set >> UNION


#   Assigning the result of union to the 1st set specified for union

fruits2 = {"apple", "pear", "limon", "grape", "cucumber", "orange"}
vegetables2 = {"cucumber", "garlic", "onion", "broccoli", "pepper"}

# Method 1: Using the symbols

fruits2 |= vegetables2
print(fruits2)

# Method 2: Using Update method

fruits2.update(vegetables2)
print(fruits2)


# Modify the Original Set >> INTERSECTION


#   Assigning the result of Intersection to the 1st set specified for intersection

fruits3 = {"apple", "pear", "limon", "grape", "cucumber", "orange"}
vegetables3 = {"cucumber", "garlic", "onion", "broccoli", "pepper"}

# Method 1: Using the symbols

fruits3 &= vegetables3
print(fruits3)

# Method 2: Using "Intersection_Update method"

fruits3.intersection_update(vegetables3)
print(fruits3)


# Modify the Original Set >> SUBTRACTION OR DIFFERENCE


#   Assigning the result of Subtraction to the 1st set specified for subtraction

fruits4 = {"apple", "pear", "limon", "grape", "cucumber", "orange"}
vegetables4 = {"cucumber", "garlic", "onion", "broccoli", "pepper"}

# Method 1: Using the symbols

fruits4 -= vegetables4
print(fruits4)

# Method 2: Using "Difference_Update method"

fruits4.difference_update(vegetables4)
print(fruits4)


# Modify the Original Set >> SYMMETRIC DIFFERENCE


#   Assigning the result of SYMMETRIC DIFFERENCE to the 1st set specified for Symmetric Difference

fruits5 = {"apple", "pear", "limon", "grape", "cucumber", "orange"}
vegetables5 = {"cucumber", "garlic", "onion", "broccoli", "pepper"}

# Method 1: Using the symbols

fruits5 ^= vegetables5
print(fruits5)

# Method 2: Using "Symmetric_Difference_Update method"

fruits5.symmetric_difference_update(vegetables5)
print(fruits5)
