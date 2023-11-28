# Program to accept the strings which contains all vowels. If string contains all vowels
# than print Accepted otherwise print the vowels not present in given string and print Not
# Accepted.

def allVowels(v_string):
    vowels = set("aeiouAEIOU")
    flag = False
    for char in v_string:
        if char not in vowels:
            flag = True
            break
    if flag:
        print("Not Accepted")
    else :
        print("Accepted")

value = input("Enter the string value: ")
allVowels(value)
