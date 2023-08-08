# Concatenation Operation in Strings

# The "+" symbol is used to concatenate numbers of list
# Here, it doesn't matter the datatype of elements present in the lists to be concatenated
# The lists mentioned are merged into a single list containing all the elements of the lists intended

fruits = ["apple", "banana", "orange"]
mixed_list = [1, "hello", 3.14, True]

new_list = fruits + mixed_list
print(new_list)

# if used '-' instead of plus, it will generate type-error
# Such operation is not possible
new_list = fruits - mixed_list
print(new_list)