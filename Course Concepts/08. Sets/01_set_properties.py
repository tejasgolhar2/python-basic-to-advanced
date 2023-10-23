# The set elements are present unordered

# The set elements doesn't have a fixed location
# Let's get this by iterating through the set

set1 = {"happy","angry","sad","excited","nervous","frustrated"}
for item in set1:
    print(item)


# Equality of Sets
# Checking two sets having same elements present in changed order

set2 = {"apple","banana","chikoo","pineapple","mango","raspberry"}
set3 = {"mango","banana","raspberry","apple","chikoo","pineapple"}
if set2==set3:
    print("The given sets are equal")
else:
    print("Ab yeh fas gaya !")


# Duplicate elements are not allowed
#  All elements are stored as a single copy, no element can be repeated

list1 = [1,2,3,4,5,1]
set4 = set(list1)
print(set4)


# Mutable object cannot be passed as a Set Element
# But a mutable object can be totally be converted into set

# It results error : Unhashable Object
tuple1 = (1,2,3)
set5 = {"one","two",tuple1,list1}
print(set5)