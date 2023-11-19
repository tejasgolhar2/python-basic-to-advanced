# Write a program to create a function to print even length word in given string

def evenLen(v_string):
    words = v_string.split(" ")
    for item in words:
        if len(item)%2 == 0:
            print(item)
            
val = input("Enter the string value: ")
evenLen(val)