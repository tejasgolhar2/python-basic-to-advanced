# Consider the code given below

year = input("Enter number of years ")  
# from here the output generated is of string dataype

weeks = 52 * int(year)
#print(type(weeks))   --->>> weeks is of integer datatype

#print("There are "+str(weeks)+" weeks in "+str(year)+" years")

# Use of f string

print(f"There are {weeks} weeks in {year} years")