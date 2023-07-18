num = int(input("Enter the number to get its factors: "))

for n in range(1,num+1): # the range includes the number itself
    if num%n == 0:
        print(n)