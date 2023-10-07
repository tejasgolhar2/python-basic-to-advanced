# MUTATION IN TUPLES
# Its not possible to implement mutation in tuples directly

# TO DO SO --
# The tuple is first converted into list
# The list not can be modified as per the requirement 
# The new list so obtained can be converted into tuple

tuple1 = ("Tejas","is","a","good,","boy")
print(tuple1)

list1 = list(tuple1)
print(list1)

list1[0] = "Kunal"
print(list1)

tuple2 = tuple(list1)
print(tuple2)