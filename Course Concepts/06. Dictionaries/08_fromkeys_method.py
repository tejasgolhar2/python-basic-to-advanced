# USING KEYS METHODS IN PYTHON

# Method: fromkeys()
#  -->> one can put the values present in the iterable as the keys of the dictionary
#  -->> if the iterable is the list, the elements of the list as keys of the dictionary 
#           will be assigned the value 'None' to each
#  -->> We can also give a default value for all the keys

names = ['robin','dustin','mike','will','jane','eleven','lucas','max','steve']
new_dict = dict.fromkeys(names,'st')
print(new_dict)
