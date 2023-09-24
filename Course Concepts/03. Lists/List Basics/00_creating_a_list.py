# Lists in Python are defined using square brackets [] and can hold elements
# of different data types, including numbers, strings, other lists, or even
# complex objects

my_list = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "orange"]
mixed_list = [1, "hello", 3.14, True]
states_in_INDIA = [
    "Maharashtra",
    "Assam",
    "Mizoram",
    "Arunachal Pradesh",
    "Rajasthan",
    "Tamilnadu",
]

# get the first element of the "my_list"
print(my_list[0])

# get the second element of the "fruits"
print(fruits[1])

# get the third element of the "mixed_list"
print(mixed_list[2])

# number of entries in the "states_in_INDIA" list
print(len(states_in_INDIA))

# changing the elements of the list
states_in_INDIA[3] = "Gujrat"
print(states_in_INDIA[3])

# negative indexing
# print the last element of the fruits list using negative indexing
# we dont need to find the index value as per the total number of elements of the list because of negative indexing
print(fruits[-1])
