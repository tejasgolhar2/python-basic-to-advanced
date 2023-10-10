def add(a,b):
    sum = a + b
    return sum

def sub(a,b):
    sub = a - b
    return sub

def mult(a,b):
    sum = a * b
    return mult

def div(a,b):
    sum = a / b
    return div

while True:
    choice = input("Choose the operation to be performed: ( + - * / )\n")
    f_num = float(input("Enter the first number: "))
    s_num = float(input("Enter the second number: "))

    if choice=='+':
        addition = add(f_num,s_num)
        print("The addition result :",addition)
    elif choice=='-':
        subtraction = sub(f_num,s_num)
        print("The subtraction result :",subtraction)
    elif choice=='*':
        multiplication = mult(f_num,s_num)
        print("The multiplication result :",multiplication)
    elif choice=='/':
        division = div(f_num,s_num)
        print("The division result :",division)
    repeat = input("Want to use calculator again: (Y/N)\n")
    if repeat=='N':
        break