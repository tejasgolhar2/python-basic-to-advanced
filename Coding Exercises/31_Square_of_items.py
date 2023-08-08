# Square of Items
# Implement a function that takes a list as a parameter and turn list items into their square.

# Example

# Input
# custom_list = [1,2,3,4,5]
# square_list(custom_list)

# Output
# [1,4,9,16,25]

def square_list(p_list):
    # TODO
    for item in range(0,len(p_list)):
        p_list[item]*=p_list[item]
    print(p_list)

custom_list = [1,2,3,4,5]
square_list(custom_list)