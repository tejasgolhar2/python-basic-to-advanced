# Use String method to replace (.) the character with (!) in below String.
#        custom_string = 'I love Python.'

custom_string = 'I love Python.' 

print(custom_string)
print(custom_string.replace(".","!"))

#  Since, strings in python are immutable and hence need use another approach to replace so -

#   This can be done using the readymade function name " replace() " in Python. 
# Its parameters are the old string and the new string with which the old needs to be replaced

custom_string2 = 'I love Python.....'
print(custom_string2.replace(".","!",2))

#   We can also pass an integer that specifies, among all the possible replacements 
# how many replacements user want to perform