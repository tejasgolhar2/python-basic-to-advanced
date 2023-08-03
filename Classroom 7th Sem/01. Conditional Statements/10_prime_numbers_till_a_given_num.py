num = int(input("Enter the range for printing prime numbers: "))

#approach 1
j = num
while(j!=0):
    i = j
    if j==2:
        print(j)
    for n in range(2,i):
        if j%n==0:
            break
        if (j%n!=0)and(n==i-1):
            print(j)
    j-= 1


'''
#approach 2
i = num

while i > 1:
    flag = False
    j = i - 1
    while j >= 2:
        if i % j == 0:
            flag = True
            break
        j -= 1

    if not flag:
        print(i)

    i -= 1
'''