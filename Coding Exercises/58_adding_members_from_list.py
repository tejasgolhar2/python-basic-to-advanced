# Adding Members from List
# Implement a function which takes as a parameter List and add elements to a Set and return a set.

# Example

# my_list = [3,4,5,1,1,3,4,9,8]
# adding_set(my_list)
# Output

# {1, 3, 4, 5, 8, 9}



# Note: The order of elements might be different.

def adding_set(my_list):
    new_set=set()
    for item in my_list:
        new_set.add(item)
    print(new_set)
        
my_list = [3,4,5,1,1,3,4,9,8]
adding_set(my_list)
