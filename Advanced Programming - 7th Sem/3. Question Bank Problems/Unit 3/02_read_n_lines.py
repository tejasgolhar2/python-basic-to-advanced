# Write a program to read first n lines from file (take value of n from user)

import os,sys

file_path = r"Advanced Programming - 7th Sem\3. Question Bank Problems\Unit 3\file_with_content.txt"

if os.path.exists(file_path):
    print("File exits in the directory..\nLets do the search :\n")
    f = open(file_path,"r")
else:
    print("File not exist !")
    sys.exit(0)

val = int(input("Enter the number of lines to be read: "))

for _ in range(val):
    line = f.readline()
    if not line:            #  When line is not present >> break out of the loop
        break
    print(line.strip())

f = f.close()

    