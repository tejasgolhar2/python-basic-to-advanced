# Write a program to find uncommon words from two strings

def unCommon(str1,str2):
    
    list1 = set(str1.split(" "))
    list2 = set(str2.split(" "))

    # we aim to return those words which are not common in both i.e., symmetric difference

    words = list1.symmetric_difference(list2)
    return words
    

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
ans = unCommon(str1,str2)

for item in ans:
    print(item)