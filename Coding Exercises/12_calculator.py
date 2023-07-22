# Implement code block which asks two numbers 
# and operation (+,-,*,/) that we want to perform on 
# these numbers and returns the result.

def calculator(a,b,c):
    if(c=='+'):
        result = a+b
        return result
    if(c=='-'):
        result = a-b
        return result
    if(c=='*'):
        result = a*b
        return result
    if(c=='/'):
        result = a/b
        return result

num1 = int(input("What is the first number? "))
num2 = int(input("What is the second number? "))
operation = input("Pick operation from this list (+,-,*,/) ")
output = calculator(num1,num2,operation)
print(num1,operation,num2,"=",output)