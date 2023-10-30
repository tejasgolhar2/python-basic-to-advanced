# Union List of Sets
#       Implement a function which takes list of sets as a parameter and returns one 
#   set which includes all elements from the given list of sets.

# list_of_sets = [
#     {10,20,30,40,50},
#     {"apple", "orange","limon","pear"},
#     {"London", "Berlin", "Paris"},
#     {"Python", "Java", "Swift"},
#     {10, "ten", "20", 20}
# ]

# Input

# convert_ls(list_of_sets)
# Output

# {'limon', 'pear', 'Java', 'orange', 10, 'Swift', 'apple', 20, 'Python', 'Paris', 30, '20', 'London', 'ten', 40, 50, 'Berlin'}



def convert_ls(v_list):
    new_set = set()
    for group in v_list:
        new_set = new_set.union(group)
    return new_set

list_of_sets = [
    {10,20,30,40,50},
    {"apple", "orange","limon","pear"},
    {"London", "Berlin", "Paris"},
    {"Python", "Java", "Swift"},
    {10, "ten", "20", 20}
]

convert_ls(list_of_sets)
