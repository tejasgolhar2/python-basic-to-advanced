# Write a program to print all odd numbers in a list

def oddNumbers(v_list):
    for num in v_list:
        if (num%2)!=0:
            print(num)


list1 = [1,2,3,4,5,6,7,8,9]
oddNumbers(list1)