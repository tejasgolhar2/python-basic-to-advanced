def factorial(v_num):
    if v_num == 1:
        return 1
    fact = v_num * factorial(v_num-1)
    return fact

num = int(input("Enter a number: "))
ans = factorial(num)
print(f"The factorial of the number {num} is {ans}")