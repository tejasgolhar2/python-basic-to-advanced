# traversal means we are going to visit each character of the string

var = "tejasgolhar"

#using for loop
print("#using for loop")
for char in var:
    print(char)

#using while loop
print("#using while loop")
index = 0
length = len(var)
while index<length:
    print(var[index])
    index+=1