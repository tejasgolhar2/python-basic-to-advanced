# Concatenate Two Lists in One List Item Wise
# Implement a function which takes two lists as parameter and return concatenation of these lists item wise.

# Example

# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# concatenate(list1, list2)
# Output

# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']

def concatenate(lista,listb):
    ans = []
    m = 0
    for item in range(len(lista)):
        for val in range(len(listb)):
            ans.append(lista[item]+listb[val])
            m+=1
    print(ans)

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
concatenate(list1,list2)