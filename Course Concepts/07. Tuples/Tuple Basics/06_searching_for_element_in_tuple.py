# Searching an element in tuple

# Approach 1: Using 'in' operator

# returns a boolean value
# Value present in tuple or not
# Index not needed to be reuturned

tuple1 = (11,22,33,44,55)
print(88 in tuple1)

# Approach 2 : Using Linear Search Algorithm

# use of enumerate fuction in Python that works similar to that of items method in dictionaries
# can return the presence of value and its index too
# alorithm to search an element in tuple

def search_element(tuple1,data):
    for index,value in enumerate(tuple1):
        if value==data:
            return f"Hurray! Element found in tuple at index value {index}"
    return "The value doesn't exist in the tuple"

tuple2 = (786,787,72)
print(search_element(tuple2,786))