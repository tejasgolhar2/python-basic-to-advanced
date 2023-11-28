# 'a' to the power 'b' - using Recursion
#        Implement a function to calculate the value of 'a' to the power 'b' using 
#   Recursion for positive integer numbers.

# Example

# power(2,4)

# Output

# 16

def power(a,b):
    if b>=0:
        if b==0:
            return 1
        else:
            return a*power(a,b-1)



print(power(2,4))