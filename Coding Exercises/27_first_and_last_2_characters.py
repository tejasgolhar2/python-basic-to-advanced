#       Implement a function which takes a string as a parameter 
# and returns new string which is made of the first 2 and the 
# last 2 chars from a given a string. If the length of given 
# string is less than 2 then return empty string.


def first_last_characters(word):
    if len(word)<2:
        return ""
    new_var = word[0:2]+word[-2:]
    return new_var


first_last_characters('appmillers')