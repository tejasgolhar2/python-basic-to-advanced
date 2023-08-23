# Format List
# Print a given list in the format that is shown below using join method.

# custom_list = [1, 2, 3, 4, 5]

# Output

# 1 | 2 | 3 | 4 | 5

custom_list = [1, 2, 3, 4, 5]
new_list = []
for item in custom_list:
    new_list.append(str(item))
output = " | ".join(new_list)
print(output)