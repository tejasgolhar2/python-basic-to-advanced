'''9. Write a program to reverse the given statement (word by word) using split and join.'''

statement = input("Enter the statement to be reversed: ")
list1 = statement.split(" ")
list2 = []
val = len(list1)

for item in range(0,val):
    list2.append(list1[val-item-1])
    
result = " ".join(list2)
print(result)