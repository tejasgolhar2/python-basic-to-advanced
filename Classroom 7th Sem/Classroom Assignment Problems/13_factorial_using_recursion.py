def factorial(num):
    if num<= 1:
        return 1
    return num * factorial(num-1)

while(True):
    num = int(input("Enter the number: "))
    print(factorial(num))

    choice = input("Want to perform factorial operation again: ")
    if choice == 'y' or choice=='Y':
        continue
    else:
        break