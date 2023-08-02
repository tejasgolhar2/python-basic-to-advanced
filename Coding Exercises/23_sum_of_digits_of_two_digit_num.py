# Create a function that takes two digit number from console 
# and returns sum of digits. e.g. if the input was 45, then 
# the output should be 4 + 5 = 9

def sum_of_two_digits():
    num = input("Enter two digit number: ")
    num1 = int(num[0:1])
    num2 = int(num[1:])
    sum = num1 + num2
    print(sum)
    
sum_of_two_digits()