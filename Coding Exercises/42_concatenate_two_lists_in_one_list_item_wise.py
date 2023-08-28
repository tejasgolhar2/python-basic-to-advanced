# Concatenate Two Lists in One List Item Wise
# Implement a function which takes two lists as parameter and return concatenation of these lists item wise.

# Example

# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# concatenate(list1, list2)
# Output

# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

def concatenate(list1, list2):
    result = []
    for i in list1:
        for j in list2:
            result.append(i+j)
    print(result)

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
concatenate(list1, list2)