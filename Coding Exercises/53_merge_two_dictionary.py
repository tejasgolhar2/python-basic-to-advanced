# Merge Two Dictionary
#       Implement a function which takes as parameter two dictionaries and merge 
#   these two dictionaries using Dictionary methods into third dictionary.

# Note : loop is not allowed

# Example

# dict1 = {'One': 2, 'Two': 2, 'Three': 3}
# dict2 = {'Three': 3, 'Four': 4, 'Five': 5}
# merge_dict(dict1, dict2)
# Output

# {'One': 2, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}


# Approach 1

def merge_dict(v_dict1,v_dict2):
    new_dict=dict()
    new_dict.update(dict1)
    new_dict.update(dict2)
    return new_dict

# Approach 2

# def merge_dict(v_dict1,v_dict2):
#     new_dict =  v_dict1.copy()
#     new_dict.update(dict2)
#     return new_dict

dict1 = {'One': 2, 'Two': 2, 'Three': 3}
dict2 = {'Three': 3, 'Four': 4, 'Five': 5}

print(merge_dict(dict1, dict2))
print(dict1)
print(dict2)