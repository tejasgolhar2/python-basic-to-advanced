# Remove Duplicates
# How can we remove duplicates from given List using Set?

# Example

# my_list = ["apple", "apple", "orange", "grape", "grape", "orange", "apple"]

# Output

# ['grape', 'apple', 'orange']


my_list = ["apple", "apple", "orange", "grape", "grape", "orange", "apple"]
my_set = set(my_list)
new_list = list(my_set)
print(new_list)