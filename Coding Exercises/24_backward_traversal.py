#       Write a while loop that starts at the last character in the string
#  and works its way backwards to the first character in the string, 
#  printing each letter on a separate line, except backwards.

val = input("Enter a string: ")
length = len(val)
index = length - 1
while index>=0:
    print(val[index])
    index-=1