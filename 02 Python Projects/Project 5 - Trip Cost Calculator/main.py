print("Welcome to the Trip Cost Calculator!")
days = input("How many days will you stay? ")
costPerNight = input("How much does hotel cost per night? $")
flightCost = input("How much does flight cost? $")
rentalCar = input(
    "If you need rental car please enter the price otherwise enter zero. $"
)
others = input("Enter other possible expenses $")
total = (
    float(days) * float(costPerNight)
    + float(flightCost)
    + float(rentalCar) * float(days)
    + float(others)
)
print(f"Total Cost: ${round(total,2)}")
