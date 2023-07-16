hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
overtime = 0
if hours > 40:
    new_rate = 1.5 * rate
    overtime = hours - 40
    pay = (40 * rate) + (overtime * new_rate)
    print("Pay:", round(pay, 2))

else:
    pay = hours * rate
    print("Pay:", round(pay, 2))
