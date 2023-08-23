# NESTED LISTS

# When one or more comma separated sublists are present in a list, its called "Nested List"

day1 = [11,22,12,14,15]
day2 = [22,11,12,15,18]
day3 = [12,9,14,14,15]
day4 = [11,2,12,14,5]

all_days = [day1,day2,day3,day4]
print(all_days)

# here, the list contains comma separated sublists



# ACCESSING NESTED LIST ELEMENTS

#      Done by the concept of indexing
#    both Positive and Negative Indexing can be implemented 

# Ex 1: Access the third element of the 4th sublist
print(all_days[3])
print(all_days[3][3])

# Ex 2: Access the first element of the sublist present in the sublist

list1 = ['a','b',['cc','dd',['eee','ffff']],'g','h']
print(list1)
print(list1[2])
print(list1[2][2])

# using positive indexing 
print(list1[2][2][0])

# using negative indexing 
print(list1[-3][-1][-2])


# UPDATING THE ELEMENTS OF THE NESTED LIST
list1[-3][2][-1] = 'xxx'
print(list1)
print(list1[-3][2][-1])