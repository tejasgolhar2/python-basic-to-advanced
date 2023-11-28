# Write a program to illustrate difference between write ( ) and append ( )
import os,sys

file_path = r"Advanced Programming - 7th Sem\3. Question Bank Problems\Unit 3\file_with_content_2.txt"

if os.path.exists(file_path):
    print("File exists in the directory !")
else:
    print("Path doesn't exists in the directory !")
    sys.exit(0)

string = input("Enter one lined content: ")
ch = int(input("Choose operation: \n1. write() \n2. append()\n"))

if ch == 1:
    with open(file_path, "w") as f:
        f.write(string)
elif ch == 2:
    with open(file_path, "a") as f:
        f.write(string)

with open(file_path, "r") as f:
    for line in f:
        print(line.strip())