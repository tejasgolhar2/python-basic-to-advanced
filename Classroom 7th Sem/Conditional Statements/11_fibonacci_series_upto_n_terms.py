n = int(input("Enter the number of terms in fibonacci sequence: "))
t1 = 0
t2 = 1

if n<=0:
    print("Invalid Input! Please enter a valid number")
elif n==1:
    print(t2)
else:
   i=1
   print(t2)
   while(i<n):
        t_next = t1 + t2
        print(t_next)
        t1 = t2
        t2 = t_next
        i+=1