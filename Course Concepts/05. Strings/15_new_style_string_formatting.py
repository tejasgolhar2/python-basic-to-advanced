# Method: NEW STYLE STRING FORMATTING

#   Use of -->> .format() operator

error_no = 1245998873651
string = "Tejas"

print("Hey {}, there is a 0x{} error!".format(string,hex(error_no)))
print("Hey {}, there is a 0x{:x} error!".format(string,error_no))
#    >>   :x   used to convert decimal to hexadecimal number

# Alternatively, by Mapping of variables
print("Hey {a}, there is a 0x{b:x} error!".format(a=string,b=error_no))
