name = input("Enter your name:\n")
length = len(name) # the number of characters are stored in length variable
print("Number of characters in name:", length)  # we printed the length that is no. of characters at output

# we cannot concatenate here the integral length with the string and we have to use type conversion for the same 
# Hence, the below line will cause an error

#print("There are "+length+"characters in the name")  