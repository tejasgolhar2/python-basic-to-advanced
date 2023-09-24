# USE OF VALUES METHOD IN PYTHON
# Its a dynamic method

custom_dict = {
    1 : 'One',
    2 : 'Two',
    3 : 'Three',
    4 : 'Four',
    5 : 'Five',
    6 : 'Six',
    7 : 'Seven',
    8 : 'Eight',
    9 : 'Nine',
}

# Use of values method
values = custom_dict.values()
print(values,'\n')


# if the dictionary is updated with changes, 
#   those are dynamically reflected in the values output 
# The values are in the form of view object which cannot be accessed using indexing
# The values are in the form of sets in Python
custom_dict[0]='Zero'
print(values,'\n')



# COnverting Values Object into list
list_values = list(custom_dict.values())
print(list_values)


# QUESTION: HOW TO CHECK WHAT IS THE KEY CORRESPONDING TO A GIVEN VALUE
# Check what is the key of the dictionary value 'five'

# Approach 1
#   Since, the dictionary have ordered sequence of keys and values

list_keys = list(custom_dict.keys())
list_values = list(custom_dict.values())

if 'five' in custom_dict.values():
    index = list_values.index('five') #-->> Got the index of the value in values list
    key = list_keys[index]            #-->> Finding the corresponding indexed value of key in keys list
    print(f"The key for the value 'five' in dictionary is {key}")

