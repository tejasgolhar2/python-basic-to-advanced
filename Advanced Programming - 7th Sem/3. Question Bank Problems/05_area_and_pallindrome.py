# Write a Program to perform following operations:
# a. Calculate Area of Circle.
# b. Check the given string is Palindrome or not.

ch = int(input("Choose Operation: \n1.Area of Circle  \n2.Check Pallindrome string\n"))

if ch == 1:
    rad = int(input("Enter the radius for the circle: "))

    import math

    pie = math.pi

    area = pie * pow(rad, 2)
    print(f"Area of circle with radius {rad} is {area}")

elif ch == 2:
    string = input("Enter the string to be checked for pallindrome: ").lower()

    string2 = string[::-1]

    if string == string2:
        print("The entered string is pallindrome")
    else:
        print("The string is not pallindrome")

else:
    print("Entered a wrong choice ! Reenter it")
