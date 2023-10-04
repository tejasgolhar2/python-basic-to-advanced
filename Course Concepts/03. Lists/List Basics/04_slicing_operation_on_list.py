# List Operations

# SLICING OF LIST

numbers = [11, 12, 113, 45]

print(numbers[:])

print(numbers[1:])
# skips the element with index = 0 and prints the rest

print(numbers[:2])
# prints elements till index < 2

print(numbers[1:3])
# prints elements from element of index = 1 to index < 3

print(numbers[2:3])
# prints the element with index 2 only

# the slicing operation works like the range functon, i.e., one elements less than the upper limit specified

#   MUTATION IN LISTS

#   The list is a mutable data-structure ( while, strings are not ) 
# This means we can update the elements of the list 
# Lets use slicing operation to update a group of elements in the list

numbers[1:3] = ["Tejas","Ramkhilavan"]
# the elements at the index 1 till index < 3 are updated as per above declaration
 
print(numbers)