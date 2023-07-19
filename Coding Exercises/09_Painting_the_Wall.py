'''
We need to paint a wall and we do not know how many cans of paint we need to buy. 
The instructions on the paint can says that 1 can of paint can cover 4 square meters of wall. 
So we need to define a function which takes as parameter  height and width of wall and  
calculates the area of the wall and based on the area we can calculate number of cans of paint that we need.

Area of wall = wall height  *  wall width
Number of cans of paint that is needed =  Area of wall ÷ coverage per can.

Example

Height = 2, Width = 5, Coverage = 4
Area of wall = 2  *  5  = 10
Number of cans of paint that is needed =  10 ÷ 4 = 2.5
But because you can't buy 2.5 of a can of paint, the result should be rounded up to 3 cans.

Hint: To round up number ceil function from math module can be used. Math.ceil()

'''
import math
def wall_parameters(height,width,coverage):

    area = height * width
    cans = area/coverage
    
    print(math.ceil(cans))
    #the use of ceil function is to fill the gap of till the next complete integer and get that integer as the output
    # that is, rounding up to the next integer value

a = int(input("Enter the height of the wall: "))
b = int(input("Enter the width of the wall: "))
c = int(input("Area Coverage: "))

wall_parameters(height=a,coverage=c,width=b)