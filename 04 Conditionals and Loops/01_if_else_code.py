print("Wel-Come to the Mortgage Eligibility Calculator")
salary = int(input("Enter yout salary in an integral format:\n$ "))

if salary>=2000:
    print("You are eligible to get mortgage")

else:
    print("OOps! You are not eligible for mortgage")
    
# the else statement is not mandatory can we can specify if condition only in the cases where else condition is not mandatory

'''In if-else condition, if the first 'if' condition evaluates true, its code is executed; otherwise
(in case the 'if' condition evaluates false ) the else block will be executed surely'''

'''

     INDENTATION
  Python relies on indentation (whitespace at the beginning of a line) 
to define scope in the code. Other programming languages often use 
curly-brackets for this purpose.

The Python style guide, known as PEP 8, recommends using four spaces for 
indentation. However, you can also use a tab character, but it's important 
to be consistent throughout your code.

'''