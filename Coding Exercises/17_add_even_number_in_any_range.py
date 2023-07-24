#       Implement a function which takes two parameters as start
#   and end of range and returns sum of even numbers within given range.


def add_even_numbers(start, end):
    sum = 0
    for number in range(start, end + 1):
        if number % 2 == 0:
            sum += number
    return sum


a = int(input("Enter starting of range: "))
b = int(input("Enter ending of range: "))
print(add_even_numbers(a, b))
