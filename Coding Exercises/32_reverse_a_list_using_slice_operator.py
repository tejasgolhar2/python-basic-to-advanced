# Reverse a given list in using Slice operator.

# Hint : Use step parameter of Slice operator - [start:stop:step]

# Approach 1

def reverseList(list):
    i = 0
    val = len(list)
    while(val):
        list[i]=len(list)-i
        i+=1
        val-=1
    return list

custom_list = [1,2,3,4,5,6,7,8,9,10]
print(reverseList(custom_list))


# Approach 2
# Reverse a List
# You can reverse a list by omitting both start and stop indices and specifying a step as -1.

L = ['a', 'b', 'c', 'd', 'e']
print(L[::-1])

# Prints ['e', 'd', 'c', 'b', 'a']

custom_list2 = [1,2,3,4,5,6,7,8,9,10,11,12]
print(custom_list2[::-1])

# the slicing starts from the last element till upto the first element as per the negative sign in step