# Write a program to perform following tuple operations given below:
# 1. Access Tuple
# 2. Update Tuple
# 3. Unpack Tuple
# 4. Join Tuple

def access(v_tuple):
    for item in v_tuple:
        print(item)

def update(v_tuple):
    # tuples are immutable
    new_tuple = list(v_tuple)

    pos = int(input("Enter the position of the element: "))
    value = int(input("Enter the value to be updated: "))
 
    new_tuple[pos-1]=value
    print(tuple(new_tuple))

def unpack(v_tuple):
    # to get every element from the tuple is called unpacking

    a,b,c,d,e = v_tuple
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)

def joinTuple(tuple1,tuple2):
    # to join the intended tuples
    
    joint_tuple = tuple1 + tuple2
    print(joint_tuple)






tuple1 = (1,2,3,4,5)
tuple2 = ('a','b','c','d','e')

ch = int(input("Choose operation:\n1. Access Tuple \n2. Update Tuple \n3. Unpack Tuple \n4. Join Tuple\n "))

if ch==1:
    access(tuple1)
elif ch==2:
    update(tuple1)
elif ch==3:
    unpack(tuple1)
else:
    joinTuple(tuple1,tuple2)