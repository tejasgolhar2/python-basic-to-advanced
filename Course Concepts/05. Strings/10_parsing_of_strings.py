# Parse the string to get the email out there from it

var = "From example.email@tejas.co.nz 05 Aug 2023 18:52 IST"

#lets find @ in the text
start_index = var.find('@')
print(start_index)

#lets find first space after the @ sign
end_index = var.find(' ',start_index)
print(end_index)

# the @ sign need not to be present
print(f"The email is : {var[start_index+1:end_index]}")