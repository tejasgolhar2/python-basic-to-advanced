# Convert Tuple to Dictionary
# Implement a function which takes a list of tuples as a parameter and convert it to a dictionary and return the dictionary.

# Example

# tuple_list = [("one", 1), ("two", 2), ("three", 3), ("four", 4)]
# convert_to_dict(tuple_list)
# Output

# {'one': 1, 'two': 2, 'three': 3, 'four': 4}

def convert_to_dict(v_tuple):
    v_dict = dict()
    for tup in v_tuple:
        v_dict[tup[0]]=tup[1]
    return v_dict

tuple_list = [("one", 1), ("two", 2), ("three", 3), ("four", 4)]
print(convert_to_dict(tuple_list))