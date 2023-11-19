#     Write a program which takes input as character and number of
# times it is going to be printed at output for taken cosecutive character 
# and number till required characters to be printed 
# Input: a1b2c3
# Output: abbccc

val = input("Enter the format as mentioned in statement: ")
output = ""
char = ""
num = 0
i = 0
while i < len(val):
    if i%2==0:
        char = val[i]
    i+=1
    if i%2!=0:
        num = int(val[i])
    output = output + (char * num)
    i+=1
print(output)