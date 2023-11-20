# Declare a class Simple_Interest having data members principal, rate_of_interest and
# no_of_years. Accept data for two objects and calculate and display simple interest for
# each object


class SimpleInterest:
    def __init__(self, principal, rate_of_interest, no_of_years):
        self.principal = principal
        self.rate_of_interest = rate_of_interest
        self.no_of_years = no_of_years

    def calculate_interest(self):
        # Simple Interest formula: SI = (P * R * T) / 100
        interest = (self.principal * self.rate_of_interest * self.no_of_years) / 100
        return interest

# Accepting data for two objects
principal1 = float(input("Enter principal amount for object 1: "))
rate1 = float(input("Enter rate of interest for object 1: "))
years1 = float(input("Enter number of years for object 1: "))

principal2 = float(input("\nEnter principal amount for object 2: "))
rate2 = float(input("Enter rate of interest for object 2: "))
years2 = float(input("Enter number of years for object 2: "))

# Creating two SimpleInterest objects
si1 = SimpleInterest(principal1, rate1, years1)
si2 = SimpleInterest(principal2, rate2, years2)

# Calculating and displaying simple interest for each object
interest1 = si1.calculate_interest()
interest2 = si2.calculate_interest()

print("\nSimple Interest for Object 1:", interest1)
print("Simple Interest for Object 2:", interest2)
