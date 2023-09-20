# Use of keys method in Python
#   Returns the dictionary keys
#   In Python 3, the keys method returns the view object which cannot be modified directly


animals = {1:'dog',2:'cat',3:'man'}
new_dictionary = animals.keys()
print(new_dictionary)

# Use case
 
for item in animals.keys():
    # the above line contains .keys() which directly tells that 'animals' is a dictionary iterable
    print(item)