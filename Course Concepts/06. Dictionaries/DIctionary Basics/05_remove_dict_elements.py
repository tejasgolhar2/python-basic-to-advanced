fruits = { 1:'apple',2:'mango',3:'banana',4:'cat'}


# USE OF pop() METHOD IN PYTHON

#  the pop gives the value corresponding to the key as the result

# case 1 : Key present in the dictionary
odd_element = fruits.pop(4)
print(odd_element)
print(fruits)

# case 2: Key not present in the dictionary
#   This will result an KeyError
#      We can use the default value to be assigned to the variable

odd_element2 = fruits.pop(5,"The entered key is absent in the dictionary")
odd_element3 = fruits.pop(6,None)
print(odd_element2)
print(odd_element3)


# USE OF popitem() METHOD IN PYTHON

# It removes the key - value pair from the dictionary
#    From python ver. 3.7, this function removes the last added key-value pair from the dictionary first

animals = {1:'dog',2:'cat',3:'man'}
exception = animals.popitem()  # < < < - - -  removes the last key-value pair of the animals
print(exception)


# USE OF del KEYWORD

#  this is used to remove the desired key-value pair in the dictionary 
del fruits[2]
print(fruits)


# USE OF clear() method 

animals.clear()  # < < --- this method removes all the elements present in the dictionary
print(animals)