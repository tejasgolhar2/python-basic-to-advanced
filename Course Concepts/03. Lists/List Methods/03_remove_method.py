# the remove method removes the first mathching element in the list

list1 = ['a','b','c','d']
list1.remove('b')
print(list1)

# if element to be removed is not present in the list, it will result ValueError
list1.remove('m')
print(list1)
