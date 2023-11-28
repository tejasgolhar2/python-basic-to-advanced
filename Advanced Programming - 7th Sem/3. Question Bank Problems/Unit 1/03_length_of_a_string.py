# Write a program to create a function and find the length of a string. (without using predefined function).

def strLen(v_string):
    count = 0
    for char in v_string:
        if char==" ":           #   Skip whitespaces
            continue
        count+=1
    return count


val = input("Enter the string value: ")
length = strLen(val)

print("String Length :",length)