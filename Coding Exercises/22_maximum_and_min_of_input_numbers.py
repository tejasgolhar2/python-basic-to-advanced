#       Write another program that prompts for a list of numbers as we did 
# in previous exercises and at the end prints out both the maximum and minimum 
# of the inputted numbers.

import sys
def check_for_float(p_input):
    try:
        val = float(p_input)
        return val
    except (ValueError, TypeError):
        print("Error, please enter numeric input")
        return False
maxim = sys.float_info.min
minim = sys.float_info.max

while True:
    val = input("Enter a number: ")
    if val =="done":
        break
    num = check_for_float(val)
    if num>maxim:
        maxim = num
    if num < minim:
        minim = num
    if (num==False):
        continue
if maxim == sys.float_info.min:
    maxim = 0.0
if minim == sys.float_info.max:
    minim = 0.0
print(f"Maximum number: {maxim}, Minimum number: {minim}")
    
# TODOf