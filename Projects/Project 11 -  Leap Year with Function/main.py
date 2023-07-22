def leapYear(num):
    """Function to check whether the arguement represents a leap year or not"""
    if num%4==0:
        if num%100==0:
            if num%400==0:
                return "Leap year."
            else:
                return "Not a Leap year."
        else:
            return "Leap year."

    else: 
        return "Not a Leap year."

year = int(input("Enter year: "))
print(leapYear(year))
