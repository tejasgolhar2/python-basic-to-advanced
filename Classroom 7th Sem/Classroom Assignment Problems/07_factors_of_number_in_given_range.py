# 7. Write a program to find the factors of the given range. For example, find the factors from 35 to 75

lower = int(input("Enter the lower range: "))
upper = int(input("Enter the upper range: "))

for i in range(lower,upper+1):
    count = 0
    print("Factors of",i,"are: ")
    for val in range(1,i+1):
        if(i%val==0):
            print(val,end=" ")
    print("\n")