# How tuples are immutable as compared to the mutable Lists

new_tuple = ("Tejas","Good","Beautiful")

print(new_tuple)
print(new_tuple[0])
print(new_tuple[1])
print(new_tuple[2])

# Let's try changing the 0th index value of the tuple

new_tuple[0] = "Sundar Boy"
print(new_tuple[0])

# This results typeError which tells that item assignment are not allwed in Tuples
# This means that Tuples are immutable
# Hence, tuples are memory efficient
# Tuples protect the integrity of the data

