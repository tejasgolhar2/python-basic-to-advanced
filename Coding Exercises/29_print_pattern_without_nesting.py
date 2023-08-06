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
    i=1
    while(i<=n):
        print(i*'* ')
        i+=1
    i=n-1
    while(i>0):
        print(i*'* ')
        i-=1
    check = input("Want to check again: (Y/N)")
    if check == 'Y':
        reInput()

def reInput():
    num = int(input("Enter maximum no. of stars in the pattern': "))   
    print_pattern(num)

num = int(input("Enter maximum no. of stars in the pattern': "))   
print_pattern(num)