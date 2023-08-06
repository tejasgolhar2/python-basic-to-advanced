# Print Pattern
#   Create a function which takes as parameter integer number (n) 
# and based on this number it prints the following start pattern 
# using nested loop and string formatting. So if n equals 5 the 
# maximum number of stars (*) will be 5 in the pattern.

# Example1

# print_pattern(5)

# Output1

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

def print_pattern(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print('*',end=" ")
        print()
    for i in range(n,0,-1):
        for j in range(i-1,0,-1):
            print('*',end=" ")
        print()
        
    check = input("Want to check again: (Y/N)")
    if check == 'Y':
        reInput()

def reInput():
    num = int(input("Enter maximum no. of stars in the pattern': "))   
    print_pattern(num)

num = int(input("Enter maximum no. of stars in the pattern': "))   
print_pattern(num)