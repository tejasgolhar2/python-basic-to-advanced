# Method to escape a particular character sequence
# The backslash (\) character is used to escape a charater sequence

# Approach 1

string1 = ''' He asked,"What's your name ?" '''
print(string1)


# Approach 2

string2 = ' He asked,"What\'s your name ?" '
print(string2)


# Approach 3

string3 = " He asked,\"What's your name ?\" "
print(string3)



# How to print Backslash character
string4 = "C:\Python\nib"
print(string4)

# we use double backslash for backslash to prevent from escaping the character sequence

string5 =  "C:\\Python\\nib"
print(string5)