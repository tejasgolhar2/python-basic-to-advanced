#       Write a program which asks for any given integer 
#   number from the console and prints out the sum of 
#   digits of given number.

num = input("Enter an integer number: ")
length = len(num)
index = length - 1
sum = 0
while length > 0 :
    sum += int(num[index])
    index-=1
    length-=1
print(sum)