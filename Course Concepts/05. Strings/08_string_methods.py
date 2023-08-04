# STRING METHODS IN PYTHON

# USE OF " DIR " KEYWORD IN PYTHON

name = "david"


# To get the type of the variable

print(type(name))


# To get list of all methods / functions for the object

print(dir(name))


# To get help with a particular method
#   Suppose I dont know about any one of the methods, say - delattr, follow the syntax as follows

help(str.isspace)
# This will result into description of the function/method asked for help
