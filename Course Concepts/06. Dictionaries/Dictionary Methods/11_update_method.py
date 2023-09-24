# USE OF UPDATE METHOD IN PYTHON

#  The new list is taken as a parameter 
#  The keys present in original dictionary common to new dictionary 
#      are updated with the corresponding values of the new dictionary

# Updating the values in key doesn't change the order in the dictionary

custom_dict = {
    1 : 'One',
    2 : 'Two',
    3 : 'Three',
    4 : 'Four',
    5 : 'Five',
}

new_dict = {
    6 : 'Six',
    7 : 'Seven',
    8 : 'Eight',
    9 : 'Nine',
    1 : 'Naya One',
    2 : 'Naya Two',
}

custom_dict.update(new_dict)

for key,value in custom_dict.items():
    print(key,value)