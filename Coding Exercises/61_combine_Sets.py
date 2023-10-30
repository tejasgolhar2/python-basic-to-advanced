# Combine Sets
#       Two sets are given write a program which creates a new set with all items from both sets 
#   by removing duplicates. And print final set to the console.

# set1 = {10,20,30,40,50}
# set2 = {60,20,50,70}
# Output

# {70, 40, 10, 50, 20, 60, 30}

# Note - The order of elements might be different


set1 = {10,20,30,40,50}
set2 = {60,20,50,70}

new_set = set1.union(set2)
print(new_set)