# Group Value Types
# Implement a function which takes a List a parameter and groups them according to their data types (integer or string) and return dictionary.

# Hint :

# Use isinstance() function to check data type.

# Use fromkeys() method to solve this challenge

# Example

# custom_list = [10, "one", "two", "ten", 20, 30, "five", 40, "nine", 50]
# group_types(custom_list)


# Output

# {
#  10: 'Integer', 
#  'one' : 'String', 
#  'two' : 'String', 
#  'ten' : 'String', 
#  20 : 'Integer', 
#  30 : 'Integer', 
#  'five' : 'String', 
#  40 : 'Integer', 
#  'nine' : 'String', 
#  50 : 'Integer'
# }

def group_types(v_list):
    lost = dict.fromkeys(v_list)
    for item in lost:
        if isinstance(item,int):
            lost[item]='Integer'
        elif isinstance(item,str):
            lost[item]='String'
    return lost

custom_list = [10, "one", "two", "ten", 20, 30, "five", 40, "nine", 50]
print(group_types(custom_list))


# Definition and Usage
# The isinstance() function returns True if the specified object is of the specified type, otherwise False.

# If the type parameter is a tuple, this function will return True if the object is one of the types in the tuple.