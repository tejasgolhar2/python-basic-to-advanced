# Remove Empty Items
#       Implement a function which takes as a parameter dictionary and removes 
#   empty items from it and return new dictionary. If there is not any empty item 
#   in the dictionary it will return itself.

# Example

# custom_dict = {
#     "name" : "Elshad",
#     "age" : 28,
#     "city" : None
# }
# remove_empty_items(custom_dict)
# Output

# {'name': 'Elshad', 'age': 28}


# Approach 1

def remove_empty_items(v_dict):
    rem_item = []
    for key,value in v_dict.items():
        if value==None:
            rem_item.append(key) 
    for item in rem_item:
        v_dict.pop(item)
    return v_dict

'''
Approach 2

def remove_empty_items(v_dict):
    for key,value in list(v_dict.items()):
        if value==None:
            v_dict.pop(item) 
    return v_dict

'''
custom_dict = {
    "name" : "Elshad",
    "age" : 28,
    "city" : None,
    "nam": None,
    "prem":"shanti"
}
print(remove_empty_items(custom_dict))