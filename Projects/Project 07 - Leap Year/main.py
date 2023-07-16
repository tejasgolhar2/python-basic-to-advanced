year = int(input("Enter  year: "))


if (year % 4) == 0:
    if year % 100 == 0:  # condition true >>> not a leap year
        if year % 400 == 0:
            print("Leap Year.")
        else:
            print("Not leap year")
    else:
        print("leap year")
else:
    print("Not leap year.")
