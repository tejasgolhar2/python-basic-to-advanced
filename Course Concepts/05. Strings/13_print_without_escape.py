
# How to print Backslash character
string1 = "C:\Python\nib"
print("Regular string: "+string1)

#   We use double backslash for backslash to prevent from escaping the character sequence 
# or to print the ROW STRING

string2 =  "C:\\Python\\nib"
print("Use of Double backslash: "+string2)

# ALTERNATIVE APPROACH TO PRINT THE ROW STRING WITHOUT ESCAPING THE SEQUENCE
#     To print the string sequence as it is, put a r OR R before the string  --- >> 

string3 = R"C:\Python\nib"
print("Use of Row String: "+string3)