# Data Types - Weeks in Years

"""
    Write a program that converts number of years to the weeks. 
    if the input was 2, 
    then the output should be 2 * 52 = 104, 
    because we have 52 weeks in 1 year.
                                        """

# TODO
year = input("Enter number of years ")
# from here the output generated is of string dataype

weeks = 52 * int(year)
# print(type(weeks))   --->>> weeks is of integer datatype

print("There are " + str(weeks) + " weeks in " + str(year) + " years")
