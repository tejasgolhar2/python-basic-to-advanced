# Count Characters in a Word
# Implement a function that takes a String as a parameter and returns a dictionary with characters as keys from the String and values are the occurrence of characters in the String. Basically we are counting the occurrence of characters in a given string and returning it as output in Dictionary.

# Example

# count_character("BABACDAS")
# Output

# {
#  'B': 2, 
#  'A': 3, 
#  'C': 1, 
#  'D': 1, 
#  'S': 1
# } 

# ToDo
def count_character(p_string):
    dictionary = dict()
    for item in p_string:
        if item not in dictionary:
            dictionary[item] = 1
        else:
            dictionary[item]+=1
    return dictionary

print(count_character("BABACDAS"))