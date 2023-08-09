# 6. Write a program to count the occurrence of vowels in a given word.

str = input("Ente a word: ")
word = str.lower()
count = 0
for i in range(0,len(word)):
    a = word[i]
    if (a == 'a') or (a == 'e') or (a == 'i') or (a == 'o') or (a == 'u'):
        count +=1
print("Number of vowels in the word",str,"are:",count)