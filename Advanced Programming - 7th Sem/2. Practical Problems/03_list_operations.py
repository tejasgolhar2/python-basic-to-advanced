# 3. Write a program to perform operations given below on the list.
#   a. Insert new element at given position.
#   b. Remove an element from the list
#   c. Sort a list
#   d. Reverse a list


def insert(v_list):
    pos = int(input("Enter the position at which element is to be inserted: "))
    value = int(input("Enter the value to be inserted: "))
    if pos<= len(v_list):
        v_list.insert(pos-1,value)
    return v_list

def remove(v_list):
    val = int(input("Enter the element is to be removed: "))
    if val in v_list:
        v_list.remove(val)
    else:
        return "Value missing in list"
    return v_list

def sort(v_list):
    ch = int(input("Ascending Sort or Descending ? (A/D) "))
    if ch=='A':
        v_list.sort()
    else:
        v_list.sort(reverse=True)
    return v_list

def reverse(v_list):
    v_list.reverse()
    return v_list


list1 = [1,2,3,4,5]
print("The given list : ",list1)

op = int(input("Choose the operation number: \n1. Insertion\n2. Removal\n3. Sort\n4. Reversal\n"))

if op == 1:
    print(insert(list1))
elif op == 2:
    print(remove(list1))
elif op==3:
    print(sort(list1))
else:
    print(reverse(list1))




