#   Union of sets

#       The union method is used to make union of given sets
# The order in which the method is used doesn't matter the final result 
# The union operation is commutative : a union b == b union a

fruits = {"apple", "pear", "limon", "grape", "orange"}
vegetables = {"cucumber", "garlic", "onion", "broccoli", "pepper"}


# Approach 1: Using union method
combination = fruits.union(vegetables)
# OR 
combination1 = vegetables.union(fruits)
print("Set 1:",combination)
print("Set 2:",combination)

# Approach 2: Using pipe operator
combination2 = fruits | vegetables
print("Set 3:",combination2)