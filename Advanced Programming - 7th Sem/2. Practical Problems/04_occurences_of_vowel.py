# 4. Write a program to find the number of Occurance of each Vowel present in the given String.

def vowelNum(string):

    vowels = {'a':0,'e':0,'i':0,'o':0,'u':0}

    for char in string:
        if char in vowels:
            val = vowels[char]
            vowels[char]=val+1

    for key,value in vowels.items():
        print(key,":",value)



word = input("Enter the string value: ")
vowelNum(word.lower())