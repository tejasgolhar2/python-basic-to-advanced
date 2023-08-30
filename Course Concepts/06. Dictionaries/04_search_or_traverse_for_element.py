# TRAVERSAL THROUGH A DICTIONARY

# we are going to loop through the dictionary and visit every key-value pair
# we have already done this for lists

dictionary1 = {
    "Tejas":"He is a very good boy that lives in Wardha",
    "Neha" : "A beautiful girl sings like a Koyal",
    "Ravi" : "He is calm minded clever boy",
} 

for item in dictionary1:
    print(item)
# this will print the keys in the dictionary only i.e., --->>>> item == key  


# TO PRINT THE DICTIONARY KEYS ALONG WITH THE VALUES

for key in dictionary1:
    print(key,"=",dictionary1[key])

# Searching for an element in dictinary