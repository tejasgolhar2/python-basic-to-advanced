animals = {"Dog", "Horse", "Cat", "Robin", "Swallow"}
birds = {"Robin", "Swallow"}
fishes = {"Boxfish", "Tuna"}


# SUBSETS

#       If a set contains elements, all of which are already present in a given set.
#   The set is said to be the subset of the given set

# Every set is a subset of itself


# Method 1: Using issubset() method

# The issubset method returns a boolean value

print(birds.issubset(animals))
print(birds.issubset(birds))

# Method 2: Using <= symbol

print(birds <= animals)


# PROPER SUBSETS

#       A proper subset is that which contains elements included already in a given set such that
#   the subset and the given set are not equal
#       A proper subset cannot be proper subset of itself

#   It can only be checked by '<' operator

print(birds < animals)



# NOTE :    Similar are the methods for "Superset","Proper Superset" and "Disjoint Set"