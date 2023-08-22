# Create a List from Two Lists
# Given two lists create a third list by picking an odd-index element from the first list and even-index elements from the second.

# list_one = [4, 12, 16, 21, 24, 28, 32]
# list_two = [5, 10, 15, 20, 25, 30, 35]
# Output

# [12, 21, 28, 5, 15, 25, 35]

list_one = [4, 12, 16, 21, 24, 28, 32]
list_two = [5, 10, 15, 20, 25, 30, 35]

# Approach 1
odd_elements = list_one[1::2]
even_elements = list_two[0::2]

final_list = odd_elements + even_elements
print(final_list)



# Approach 2
# odd_elements = list_one[1::2]
# even_elements = list_two[0::2]

# list3 = []

# list3.extend(odd_elements)
# list3.extend(even_elements)
# print(list3)



# Approach 3
# new_list = []
# for item in list_one:
#     ind1 = list_one.index(item)
#     if (ind1%2)==1:
#         new_list.append(item)
        
# for item in list_two:
#     ind2 = list_two.index(item)
#     if (ind2%2)==0:
#         new_list.append(item)   
# print(new_list)
