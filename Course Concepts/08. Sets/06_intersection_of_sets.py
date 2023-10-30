# Intersection of Sets

# The set intersection results a new set having elements common to all of the given sets
# The intersection method is commutative as in case of Union

fruits = {"apple", "pear", "limon", "grape", "cucumber", "orange"}
vegetables = {"cucumber", "garlic", "onion", "broccoli", "pepper"}



# Approach 1: Using intersection method

set1 = fruits.intersection(vegetables)
set2 = vegetables.intersection(fruits)

print("Set 1:",set1)
print("Set 2:",set2)



# Approach 2 : Using Ampersand Operator

set3 = fruits & vegetables
print("Set 3:",set3)



# For multiple sets to be intersected

flowers = {"Mango","cucumber"}

set4 = set.intersection(fruits,vegetables,flowers)
print("Set 4:",set4)