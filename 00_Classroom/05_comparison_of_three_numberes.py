var1 = int(input("Enter first integer number:"))
var2 = int(input("Enter the second number: "))
var3 = int(input("Enter the third number: "))

if((var1>var2)and(var1>var3)):
    print("The entered variable",var1,"is the greatest")
elif((var2>var1)and(var2>var3)):
    print("The entered variable",var2,"is the greatest")
else:
    print("The entered variable",var3,"is the greatest")