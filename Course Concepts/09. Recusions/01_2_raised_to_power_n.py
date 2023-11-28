def PowerofTwo(n):
    assert type(n)==int and n>=0, "The value should be a positive integer"
    if n==0:
        return 1
    if n==1:
        return 2
    return 2 * PowerofTwo(n-1)

val = int(input("Enter the value: "))
print(PowerofTwo(val))