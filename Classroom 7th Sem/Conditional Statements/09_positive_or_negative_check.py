try:
    num = int(input("Enter the number value to be checked: "))
except ValueError:
    print("Invalid data input\nPlease enter correct details by restarting the code")
else:
    if num>0:
        print("Number is positive.")
    elif num<0:
        print("Number is negative.")
    else:
        print("Its value is zero")