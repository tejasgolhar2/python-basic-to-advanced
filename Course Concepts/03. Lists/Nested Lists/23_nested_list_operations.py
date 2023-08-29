# The methods and fuctions that we used for simple list are opearable on nested lists also

list1 = ['a','b',['cc','dd',['eee','ffff']],'g','h']

# APPEND METHOD
# Negative indexing is not used to append in Nested List

# append element to the main list
list1.append('i')
print(list1)

# append element into sublist
list1[2][2].append('jjj')
print(list1)


# INSERT METHOD
#  to insert element to the position what intended in the list

# to the main list
list1.insert(0,'oooo')
print(list1)
# here, list becomes : ['oooo', 'a', 'b', ['cc', 'dd', ['eee', 'ffff', 'jjj']], 'g', 'h', 'i']

# to the sublist
list1[3][2].insert(0,'mmmm')
print(list1)


# USE OF POP METHOD
# USE OF DEL FUNCTION
# USE OF LEN FUNCTION

# LOOPING THROUGH THE NESTED LIST
# the below method can't be used for integer nested list

list2 = ['1','2',['3','4','5',['11','12','22']],'66','77','88','99']
for item in list2:
    for item1 in item:
        for item2 in item1:
            print(item2)

list3 = [[1,2],[3,4,5],[66,77,88,99]]
for item in list3:
    for item1 in item:
        print(item1)
    