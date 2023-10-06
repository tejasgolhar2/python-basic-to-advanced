#  UNPACKING TUPLES

#       To assign the the multiples tuple values to different tuples simultaneously,
#   The Tuples are provided with the additional functionality of UNPACKING

#        We can assign same value to multiple tuples simultaneously
#   Similarly, for multiple tuples, the values can be assigned in a single statement


# Assigning same value to different tuples

a = b = c = d = (11,12,21)
# the paretheses are optional in Python Tuples
print(a)
print(c)
print(b)
print(d)


# Assigning different values to different tuples

a1,b2,c3 = (1,),(2,),(3,)
print(a1)
print(c3)
print(b2)


# Accessing/Unpacking Every element from tuple 

new_tuple = (11,25,45,78)
A,B,C,D = new_tuple

print(A)
print(B)
print(C)
print(D)


# # NOTE :  Unpacking of list is not advisable

#   Since, before unpacking the individual element of the list
#   if we modified the list content, then it will result an error that - - > >
#           THERE ARE TOO MANY VALUES TO UNPACK 
#        But this is not the case with tuples, since they are immutable