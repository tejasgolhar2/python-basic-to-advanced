# Write a program to print characters present on even or odd positions of string variable

var = input("Enter a string value: ")

print("APPROACH 1 : Using concept of slicing in strings") 

print("Characters on Even Position: "+var[1::2])

#   In the above slicing syntax, the first 0 is the start index 
# of the slicing, till end of the string by a step of 2 characters


print("APPROACH 2 : Using While Loop")

i = 1
while i<len(var):
    print(var[i])
    i+=2
# all the even locationed characters are printed on the new line


print("APPROACH 3 : Using For Loop")

j = 1
for char in var:
    if j < len(var):
        print(var[j])
    j+=2