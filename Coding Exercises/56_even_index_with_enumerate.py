# Even Index with Enumerate
#       Implement a function which takes as a parameter a tuple and return 
#   a new tuple but only have even index elements from original tuple.

# Hint : Use enumerate() function

# Example

# my_tuple = ("a", "b", "c", "d", "e", "f", "g")
# even_index_items(my_tuple)
# Output

# ('a', 'c', 'e', 'g')

def even_index_items(v_tuple):
    n_list = []
    for index,value in enumerate(v_tuple):
        if index%2 == 0:
            n_list.append(value)
    return tuple(n_list)

my_tuple = ("a", "b", "c", "d", "e", "f", "g")
print(even_index_items(my_tuple))