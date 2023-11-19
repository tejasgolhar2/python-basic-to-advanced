# Write a program to find second largest number in a list.

def secondLargest(v_list):
    v_list.sort(reverse=True)
    print(v_list[1])


list1 = [1,2,3,4,5,6,7,8,9]
secondLargest(list1)