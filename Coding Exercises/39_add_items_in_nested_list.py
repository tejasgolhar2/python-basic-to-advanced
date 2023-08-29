# Add Item in Nested List
# Given a list as shown below and add item 7000 after 5000 and print out final list to the console.

# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# Output

# [10, 20, [300, 400, [5000, 7000, 6000], 500], 30, 40]

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].insert(1,7000)
print(list1)