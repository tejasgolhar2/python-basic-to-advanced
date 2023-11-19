# 6. Write a program to demonstrate exception handling in Python.

# Exception handling for wrong input given by user for the program to caluculate area of square

flag = True

while(flag):
    try: 
        side = float(input("Enter the side length of the squre: "))
    except ValueError:
        print("You have entered improper value !\nPlease try once again..\n")
        continue
    else:
        area = pow(side,2)
        print("The area of the square :",area)
        flag=False
        