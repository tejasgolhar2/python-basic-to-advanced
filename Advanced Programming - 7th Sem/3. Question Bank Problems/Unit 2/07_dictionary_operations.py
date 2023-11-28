# Write a program to perform following dictionary operations given below:
# 1. Access Item
# 2. Change Item
# 3. Add Item
# 4. Remove Item



def access(v_dict):
    for key,item in v_dict.items():
        print(item)

def change(v_dict):
    item = int(input("Enter the item key whose value to be changed: "))
    value = input("Enter the value to be replaced : ")
    
    for index in v_dict:
        if index == item:
            v_dict[item] = value
    
    print(v_dict)
  
def add(v_dict):
    key = int(input("Enter the key to be added: "))
    value = input("Enter the associated value for the key : ")
    v_dict[key]=value
    print(v_dict)
    

def remove(v_dict):
    key = int(input("Enter the key for the item pair to be removed: "))
    del v_dict[key]
    print(v_dict)
    


dict1 = {1:"one",2:"two",3:"three",4:"four",5:"five"}

ch = int(input("Choose operation:\n1. Access Item \n2. Change Item\n3. Add Item\n4. Remove Item\n"))

if ch==1:
    access(dict1)
elif ch==2:
    change(dict1)
elif ch==3:
    add(dict1)
else:
    remove(dict1)