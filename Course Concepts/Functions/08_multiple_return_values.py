
def print_formatted_name(a,b):
    formatted_name = a.title()
    formatted_surname = b.title()

    if a=="" or b=="":
        return "Name or Surname can't be empty"
    #for the condition to be true, the output will be "None"
    #we can also write a message to be displayed ahead of return when the condition becomes true

    result = (f"{formatted_name} {formatted_surname}")
    return result

    print("This won't be printed")

# Whatever content is written after the return statement of the function, that part of the code wont be executed
# the return keyword tells the interpreter that its the end of the function and you should now exit the function

'''
    Consider the case,
        where the user gives empty string OR NULL as input. In such condition the code results nothing in the output
        
    To prevent this, we can use "return" keyword without specifying anything in front of it... this will result into 
    "None" as the result

    '''
          

name = input("Enter name: ")
surname = input("Enter surname: ")

output = print_formatted_name(a=name,b=surname)
print(output)

