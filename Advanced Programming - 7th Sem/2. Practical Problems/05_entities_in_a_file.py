# 5. Write a program to print the number of lines, words, and characters present in the given file.

import os,sys

f_path = "Classroom 7th Sem\Practical Problems\/05_file_entities.txt"

if os.path.exists(f_path):
    print("File already exists")
    f = open("Classroom 7th Sem\Practical Problems\/05_file_entities.txt","r")

else:
    print("File not present")
    sys.exit(0)

lines = words = characters = 0

for line in f:
    lines += 1

    words_list = line.split(" ")
    words += len(words_list)

    characters += len(line)

print("Number of lines: ",lines)
print("Number of words: ",words)
print("Number of characters: ",characters)

f= f.close()



