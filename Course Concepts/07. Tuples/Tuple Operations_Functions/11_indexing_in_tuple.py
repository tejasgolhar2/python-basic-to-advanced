# Use of Index Operator in PYthon
# The index of first occurence of the specified element is returned using the operator

names = ("Ravi","Pratik","Utkarsh","Nakul","Rudra")


# Case 1 : Element Present In TUple
index_1 = names.index("Pratik")
print(index_1)



# Case 2 : Element Not Present in Tuple
#  It results error in the code
# index_2 = names.index("Tejas")
# print(index_2)



# Case 3: WHen the tuple contains same element with mutiple occurences 
# The index of the element with its first occurence is returned 
tuple1 = (45,23,43,452,865763,85,0,758,452)
print(tuple1.index(452))