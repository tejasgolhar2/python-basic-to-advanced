# The below are the different functions that can be used over lists in Python

list1 = [ 'mango','apple','kartik','tambo']
list2 = [1,89,56,2]

# length function
print(len(list1))

# maximum function
print(max(list1))

# minimum function
print(min(list1))

# sum function
# The sum function can only be used with the list containing numbers otherwise will give 'TypeError' 
print(sum(list2))
# print(sum(list1))

# del function (delete function)
# It is similar to that of the pop method in Python Lists
# The deletion operation can be done by accessing index of the items

del list1[-1]
print(list1)

del list2[1]
print(list2)

