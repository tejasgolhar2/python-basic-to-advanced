# Custom Deep Copy for List Values
# Implement custom deep copy method for a dictionary where the values are lists.

# Example

# original_dict = {
#     "names" : ["Elshad", "John", "Edy"],
#     "numbers" : [1,2,3,4,5]
# }
 
# copied_dict = deep_copy(original_dict)
# copied_dict["names"].append("Jack")
# copied_dict["numbers"].append(6)
 
# print(original_dict)
# print(copied_dict)
# Output

# {
#     'names': ['Elshad', 'John', 'Edy'], 
#     'numbers': [1, 2, 3, 4, 5]
# }
 
# {
#     'names': ['Elshad', 'John', 'Edy', 'Jack'], 
#     'numbers': [1, 2, 3, 4, 5, 6]
# }


# Approach 1 : Using function

# import copy
# original_dict = {
#     "names" : ["Elshad", "John", "Edy"],
#     "numbers" : [1,2,3,4,5]
# }
 
# copied_dict = copy.deepcopy(original_dict)
# copied_dict["names"].append("Jack")
# copied_dict["numbers"].append(6)
 
# print(original_dict)
# print(copied_dict)


# Approach 2 : Custom function

def deep_copy(v_dict):
    new_dict = dict()
    

    for key,value in v_dict.items():
        val_list = value.copy()
        new_dict[key]=val_list
    return new_dict

original_dict = {
    "names" : ["Elshad", "John", "Edy"],
    "numbers" : [1,2,3,4,5]
}
 
copied_dict = deep_copy(original_dict)
copied_dict["names"].append("Jack")
copied_dict["numbers"].append(6)
 
print(original_dict)
print(copied_dict)