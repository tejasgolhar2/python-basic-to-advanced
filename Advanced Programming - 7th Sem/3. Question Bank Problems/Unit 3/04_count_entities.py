# Write a program to open an existing file in read mode and count the no. of spaces, new
# line, and characters in file.

import os,sys

file_path = r"Advanced Programming - 7th Sem\3. Question Bank Problems\Unit 3\file_with_content.txt"

if os.path.exists(file_path):
    print("File exits in the directory...")
    f = open(file_path,"r")
else:
    print("File not exist !")
    sys.exit(0)

spaces = 0
newlines = 0
characters = 0

for line in f:
    for char in line:
        if char == " ":
            spaces += 1
        elif char == "\n":
            newlines += 1
        else:
            characters += 1

print(f"Spaces : {spaces}")
print(f"Newlines: {newlines}")
print(f"Characters: {characters}")

f = f.close()

    