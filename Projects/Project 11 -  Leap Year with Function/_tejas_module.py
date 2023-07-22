
pi = 3.142
g = 9.8
name = "Tejas"
surname = "Golhar"
full_name = "Tejas Sudhakar Golhar"
address = "California, UK"
contact_num = "9XXVVTTUU55"
mail_id = "test@gmail.com"

#leap year function definition
def leapYear(num):
    if num%4==0:
        if num%100==0:
            if num%400==0:
                print("Leap year.")
            else:
                print("Not a Leap year.")
        else:
            print("Not a Leap year.") 
    else:
        print("Not a Leap year.") 