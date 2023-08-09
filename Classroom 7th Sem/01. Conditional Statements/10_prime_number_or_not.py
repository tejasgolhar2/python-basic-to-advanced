# 4. Write a program to check if the given number is prime or not.

num = int(input("Enter a number to be checked: "))

count = 1
val = num -1
if num==1:
    print("Entered number is neither prime nor composite")
elif num<=0:
    print("Please enter a valid number")
while (val > 1):
    if num % val == 0:
        print("{} is not a prime number".format(num))
        quit()
    if (num % val) != 0:
        if (count == (num-2)):
            print("{} is a prime number".format(num))
        count +=1 
        val-=1