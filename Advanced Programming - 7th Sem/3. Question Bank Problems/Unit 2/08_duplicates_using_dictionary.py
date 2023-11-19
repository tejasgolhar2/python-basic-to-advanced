# Write a program to find all duplicate characters in strings using dictionary.

def duplicate(v_string):
    n_dict = dict()
    for char in v_string:
        if char not in n_dict:
            n_dict[char] = 1
        else:
            val = n_dict[char]
            n_dict[char] = val + 1

    for key,value in n_dict.items():
        if value >= 2:
            print(key)


value = input("Enter the string value for checking duplicates: ")
duplicate(value)