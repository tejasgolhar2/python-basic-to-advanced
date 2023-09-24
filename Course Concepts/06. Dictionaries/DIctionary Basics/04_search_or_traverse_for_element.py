# TRAVERSAL THROUGH A DICTIONARY

# we are going to loop through the dictionary and visit every key-value pair
# we have already done this for lists

dictionary1 = {
    "Tejas":"A very good boy",
    "Neha" : "A beautiful girl",
    "Ravi" : "Calm minded clever boy",
} 

for item in dictionary1:
    print(item)
# this will print the keys in the dictionary only i.e., --->>>> item == key  


# TO PRINT THE DICTIONARY KEYS ALONG WITH THE VALUES

for key in dictionary1:
    print(key,"=",dictionary1[key])


#Use of IN and NOT IN operator

# Searching for an element in dictinary 
# The IN and NOT IN Operators search for the intended key whether to be present in the dictionary or not
my_dict = {
    1 : 'one',
    2 : 'two',
    3 : 'three'
}

print(1 in my_dict) # search for whether 1 is present as one of the keys in the dictionary or not.
print('one' in my_dict)  # the seaching scope is of the keys only and the values in the dictionary