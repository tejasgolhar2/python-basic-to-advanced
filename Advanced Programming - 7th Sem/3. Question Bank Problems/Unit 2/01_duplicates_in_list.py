# Write a program to print duplicates from list of integers.

def giveDuplicates(v_list):
    check = []
    for element in v_list:
        if element not in check:
            check.append(element)
        else:
            print(element)


list1 = [1,1,2,3,4]
giveDuplicates(list1)