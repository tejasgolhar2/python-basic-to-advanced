# the slicing is similar to the use of range function in Python

var1 = "TejasGolhar"
# slice from index Zero to the given max value of index

print(var1[0:6])
# the output will have one element less than the maximum of the entered slicing index for the string

var2 = "RaviShastri"
# slice string with mentioning the start index and giving the max value of index

print(var2[3:6])
# the output will have one element less than the maximum of the entered slicing index for the string

var3 = "KiranMalhotra"
# slice string without mentioning the start and giving the max value of index

print(var3[:6])
# defalt in the case, start slicing index is Zero
# the output will have one element less than the maximum of the entered slicing index for the string

var4 = "ChaturRamlingam"
# slice string with mentioning the start of the slice and without the end index value

print(var4[4:])
# the output all the rest element of the string from the start of the slicing index given

print(var4[:])
#the string is printed as it is