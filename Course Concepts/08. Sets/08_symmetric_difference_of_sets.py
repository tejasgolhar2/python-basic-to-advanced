# SYMMETRIC DIFFERENCE

#       Getting those elements from the given sets not common in both
#       Means, those elements which are unique in both sets

#   Its different from "Union", since union contains all the elements in given sets to be united

fruits = {"apple", "pear", "limon", "grape", "cucumber", "orange"}
vegetables = {"cucumber", "garlic", "onion", "broccoli", "pepper"}


# Method 1: Using built-in "symmetric_difference()" function

syn_diff = fruits.symmetric_difference(vegetables)  # order doesn't matter
print(syn_diff)


# Method 2: Using Power Operator

sim_diff = fruits ^ vegetables  # order doesn't matter
print(sim_diff)
