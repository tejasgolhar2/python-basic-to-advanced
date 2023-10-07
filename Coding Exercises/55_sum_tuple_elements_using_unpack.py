# Sum Tuple Elements using Unpack
#   Write a Python program to unpack tuple in several variables and 
# print out sum of these variables, the output must be as shown below.

# Example

# my_tuple = (10, 40, 80, 90)

# Output

# 10+40+80+90=220

my_tuple = (10, 40, 80, 90)
a,b,c,d = my_tuple

# lets format the string output
print(f"{a}+{b}+{c}+{d}={a+b+c+d}")