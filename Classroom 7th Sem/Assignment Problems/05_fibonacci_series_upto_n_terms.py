# 5. Write a program to print the Fibbonacci series until the given number. (0 1 1 2 3 5 8 13 21 34 55...)

n = int(input("Enter the number of terms in fibonacci sequence: "))
t1 = 0
t2 = 1

if n<=0:
    print("Invalid Input! Please enter a valid number")
elif n==1:
    print(t1)
else:
   i=2
   print(t1)
   print(t2)
   while(i<n):
        t_next = t1 + t2
        print(t_next)
        t1 = t2
        t2 = t_next
        i+=1