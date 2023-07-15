try:
    hours = float(input("Enter Hours: "))
except ValueError:
    print("Error, please enter numeric input for Rate")
    quit()

try:
    rate = float(input("Enter Rate: "))
except ValueError:
    print("Error, please enter numeric input for Rate")
    quit()

overtime = 0
if hours > 40:
    new_rate = 1.5 * rate
    overtime = hours - 40
    pay = (40 * rate) + (overtime * new_rate)
    print("Pay:", round(pay, 2))

else:
    pay = hours * rate
    print("Pay:", round(pay, 2))

print("Thank You for using Gross Pay System")
