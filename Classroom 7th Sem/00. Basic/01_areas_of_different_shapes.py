
# 1. Program to calculate the area of a circle, rectangle, square, and triangle.

# Area of Square
side1 = float(input("Enter the side magnitude of the square:"))
area = pow(side1,2)
print("The area of square for the entered side is: ",area)

# Area of Circle
pi = 3.142
rad = float(input("Enter the value of radius of the circle\n"))
area = pi * rad * rad
print('The area of circle with radius',rad,'is',area)


# Area of Rectangle
len = float(input("Enter the length of the rectangle:\n"))
bread = float(input("Enter the breadth of the reactangle:\n"))
area = len * bread
print("The area of the rectangle for the entered parameters is : ", area)

# Area of Triangle
height = float(input("Enter the height of the triangle: "))
base = float(input("Enter the base lenght of the traingle: "))
area = 0.5 * base * height
print("Area of triangle is : ", area)
