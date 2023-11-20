# Write a program to count words in Text file

import os,sys

file_path = r"Advanced Programming - 7th Sem\3. Question Bank Problems\Unit 3\file_with_content.txt"

if os.path.exists(file_path):
    print("File exits in the directory...")
    f = open(file_path,"r")
else:
    print("File not exist !")
    sys.exit(0)

wc = 0

for line in f:
    line_words = line.split(" ")
    wc += len(line_words)
    
    
print(f"Word Count: {wc}")

f = f.close()

    