# extend method is superior than the append method
# here, a complete iterable (an element or a list), can be added to the list at its end 

list1 = ['a','b','c','d']
list2 = ['e','f','g']

list1.extend(list2)
print(list1)

# NOTE: We are attempting to extend the original list1 which during printing, is passed as a parameter
