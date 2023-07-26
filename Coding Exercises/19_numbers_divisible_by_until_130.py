#       Implement a function which takes a given ordered list 
#   as a parameter and displays numbers divisible by 5 and if a 
#   number is greater than 130 display STOP in the console.

def numbers_divisible_byfive(p_list):
    for number in p_list:
        if number>130:
            print("STOP")
            break
        if number%5==0:
            print(number)

list1 = [12, 15, 32, 40, 52, 75, 122, 132, 150, 180, 200] 
numbers_divisible_byfive(list1)