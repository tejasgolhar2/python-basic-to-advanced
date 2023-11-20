import os,sys

file_path = r"Advanced Programming - 7th Sem\3. Question Bank Problems\Unit 3\file_with_content.txt"

if os.path.exists(file_path):
    print("File exits in the directory..\nLets do the search :\n")
    f = open(file_path,"r")
else:
    print("File not exist !")
    sys.exit(0)

lineNum = 0
value = input("Enter the word to be searched: ")
flag = False
for line in f:
    lineNum+=1
    words =  line.split(" ")
    if value in words:
        print(f"The word '{value}' found at line no : {lineNum}'")
        flag= True

if not flag:
    print(f"The word {value} not found in the file")

f = f.close()

    