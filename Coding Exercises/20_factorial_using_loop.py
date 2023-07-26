# Implement a function that takes an integer number as a parameter and returns factorial of this number.

# Factorial Equation (!)

# 5! = 5 x 4 x 3 x 2 x 1 = 120

# 4! = 4 x 3 x 2 x 1 = 24

# If input is 0 then the return p_numue will be: The factorial of 0 is 1

# if input is a negative number then the return p_numue will be: Factorial does not exist for negative numbers

def factorial(p_num):
    fact = 1
    if p_num<0:
        print("Factorial does not exist for negative numbers")
    elif p_num==0:
        print("The factorial of 0 is 1")
    else:
        for numbe in range(1,p_num+1):
            fact = fact * p_num        
        print(f"The factorial of {p_num} is {fact}")

factorial(4) 
factorial(-1)