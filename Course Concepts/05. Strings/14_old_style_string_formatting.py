# Method: OLD STYLE FORMATTING OF STRINGS

error_no = 1245998873651
string = "Tejas"

print("Hello %s, there is a 0x%x error! " % (string, error_no))
#   %s is the format specifier for the string and the variables are taken in parenthesis with % sign at the beginnig
# NOTE : %x is the format specifier to convert a given decimal value of corresponding variable into hex()

# Alternatively,  can be done by mapping as -

print("Hello %(1)s, there is a 0x%(2)x error!" %{"2":error_no,"1":string})
