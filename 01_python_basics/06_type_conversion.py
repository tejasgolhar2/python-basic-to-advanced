name = input("Enter your name:\n")

length = len(name)  # the number of characters in the string name is stored in length variable

#print("There are total "+length+" number of characters in the name")
#    ^^--<<<---- concatenation of string with integer throws error

print("The datatype of length variable is ", type(length), "\n")
# It yields that the datatype of length is integer

# Lets do the typeconversion of integer into string so that the concatenation wont give any error
nlength = str(length)
print("The changed datatype of the new length variable is ", type(nlength), "\n")
# It shows the datatype is changed to string 

print("There are total " + nlength + " number of characters in the name")
#concatenation by typeconversion successfull