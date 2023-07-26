#        Write a program which repeatedly reads numbers until the
#   user enters "done". Once “done” is entered, print out the total, 
#   count, and average of the numbers.

#      If the user enters anything other than a number, detect their mistake
#   using try and except and print an error message and skip to the next number.
 


def checkNum(num):
    try:
        val = float(num)
        return val
    except (ValueError,TypeError):
        print("Error, please enter a numeric input")
        return False
        
#num = input("Enter a number: ")
tot = 0.0
avg = 0.0
count = 0

while True:
    num = input("Enter a number: ")
    if num =="done":
        break
    val = checkNum(num)
    if val==False:
        continue
    tot += val
    count += 1
    if count != 0:
        avg = tot/count
print(f"{tot} {count} {avg}")

    
