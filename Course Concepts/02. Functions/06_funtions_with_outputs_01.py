
#funtions with return value

def calculation():
    result = 1+2
    return result



value1 = calculation()
print(value1)

#       The console won't give any result as the value of the task is calculated and 
# returned to the function call but it wasn't stored somewhere and asked to be get printed
#          Hence to get the value from the function, it is stored in a variable and 
# is accessed by contacting the variable name



#funtions without return value

def name_print():
    print("Hello Tejas")
    print("Hello Tejas")
    
value2 = name_print()
print(value2)

# here the console will show "None" as the function don't have any return type.
