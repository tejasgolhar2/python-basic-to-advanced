def factorial(n):
    assert type(n)==int and n>=0 , "n must be a positive integer number"
    if n in [0,1]:
        return 1
    return n*factorial(n-1)

val = int(input("Enter a value: "))
print(factorial(val))