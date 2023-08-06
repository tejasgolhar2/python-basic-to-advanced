# Format a String
#       Use find and string slicing to extract the portion of the 
# string after the colon character and then use the float function 
# to convert the extracted string into a floating point number.

custom_string = 'X-MAPDS-Confidence:0.8475' 
start = custom_string.find(':')
val = custom_string[start+1:]
print(float(val))