#print odd numbers from 1 to 50  if number to be printed is greater than 40, stop printing the odd number

for number in range(1,51):
    if number>40:
        break
    if number%2==1:
        print(number)
