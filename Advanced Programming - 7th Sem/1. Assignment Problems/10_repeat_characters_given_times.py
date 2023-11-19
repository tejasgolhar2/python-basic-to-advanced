# 10. Write a program to perform the operation given below. 
# Input: A5B4C3
# Output: AAAAABBBBCCC

pattern = input("Enter the desired pattern to be obtained: ")
val = len(pattern)

for item in range(1,val+1):
    if item%2 == 1:
        char = pattern[item-1]
        mult = int(pattern[item])
        print(char * mult, end="")
    item+=1
