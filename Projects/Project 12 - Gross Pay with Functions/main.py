def compute_pay(h,r):
    overtime = 0
    if h > 40:
        new_rate = 1.5 * r
        overtime = h - 40
        pay = (40 * r) + (overtime * new_rate)
        print("Pay:", round(pay, 2))
    else:
        pay = hours * rate
        print("Pay:", round(pay, 2))


def checkInput(val):
    try:
        # Note that string can also be converted into float but the string to be
        # converted should be of valid numeric type otherwise the block will result 
        # into value error
        num = float(val)
        return num
    except ValueError:
        print("Error, please enter numeric input")
        quit()


hours = input("Enter Hours: ")
hours = checkInput(hours)
rate = input("Enter Rate: ")
rate = checkInput(rate)
compute_pay(hours,rate)
