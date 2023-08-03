# Use of format function

#approach 1
# here we specified the variable name directly into the format function

name = "Tejas"
profession = "Student"
print("My name is {} and my current profession is {}".format(name,profession))


#approach 2
# here we have printed the characters in the string using the index values

print("My name starts with letter {} and ends with letter {}".format(name[0],name[-1]))


#approach 3
#here we put random variable in paranthesis and then assigned each random variable the actual variable value
print("My name is {x} and current profession is {y}".format(x=name,y=profession))