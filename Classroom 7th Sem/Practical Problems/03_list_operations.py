def insert(v_list):
    pos = int(input("Enter the position at which element is to be inserted: "))
    value = input("Enter the value to be inserted: ")
    if pos<= len(v_list):
        v_list.insert(pos-1,value)
    print("list after insertion is ",v_list)

list1 = [1,2,3,4,5]
print("The given list is ",list1)
op = input("Choose the operation number: \n1. Insertion\n2. Removal\n3. Sort\n4. Reversal\n")
if op == 1:
    insert(list1)




