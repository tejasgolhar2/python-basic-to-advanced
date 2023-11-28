# Program to find the longest number in file.

import sys,os

file_path = r"Advanced Programming - 7th Sem\3. Question Bank Problems\Unit 3\file_with_content.txt"

if os.path.exists(file_path):
    print("File exists in the directory .. Lets Search : ")
else:
    print("File donesn't exits !")
    sys.exit(0)

f = open(file_path,"r")
all_num = list()

for line in f:
    numbers = line.split(" ")
    for num in numbers:
        if num.isdigit():
            all_num.append(int(num))
if all_num:
    longest_num = max(all_num, key = lambda x: len(str(x)))

print(f"The longest number in the file : {int(longest_num)}")

f = f.close()