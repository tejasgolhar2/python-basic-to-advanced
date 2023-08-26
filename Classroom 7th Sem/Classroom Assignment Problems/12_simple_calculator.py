# 12. Write a program to design a simple calculator.

def takeinput():
    a = float(input("Enter the first value: "))
    b = float(input("Enter the second value: "))
    return a,b

def add():
    a,b = takeinput()
    sum = a + b
    print(sum)

def sub():
    a,b = takeinput()
    sub = a - b
    print(sub)

def mult():
    a,b = takeinput()
    mult = a * b
    print(mult)

def div():
    a,b = takeinput()
    div = a / b
    print(div)

def mod():
    a,b = takeinput()
    mod = a % b
    print(mod)

def power():
    a,b = takeinput()
    power = a + b
    print(power)

while(True):
    opt = input("Choose the operation to be performed: (+ - * / % ^)")
    if opt=='+':
        add()
    if opt=='-':
        sub()
    if opt=='*':
        mult()
    if opt=='/':
        div()
    if opt=='%':
        mod()
    if opt=='^':
        power()
        
    choice = input("Want to use caluculator again: (Y/N)")
    if choice=='y'or choice=='Y':
        continue
    else:
        break