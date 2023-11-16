# Find Most Frequent Item

#   Implement a function which takes a tuple as a parameter and returns another 
# tuple with two elements. First element is the most frequent item and the second 
# element of number of repetition.

# Hint: Use count() method

# Example

# my_tuple = ("a","b","c","d","e","a","c","e","b","e","c","a","f","e","r")
# most_frequent(my_tuple)
# Output

# ('e', 4)


def most_frequent(v_tuple):
    elements = list()
    counts = list()
    for item in v_tuple:
        count = 1
        if item not in elements:
            elements.append(item)
            counts.append(count)
        elif item in elements:
            val = counts[elements.index(item)]
            val += 1
            counts[elements.index(item)] = val
    max_count = 0
    for element in counts:
        max_count = max(max_count,element)

    index_max = counts.index(max_count)
    repeat = elements[index_max]
    return (repeat,max_count)

    


    new_tup = tuple()
    
    return new_tup



my_tuple = ("a","b","c","d","e","a","c","e","b","e","c","a","f","e","r")
print(most_frequent(my_tuple))