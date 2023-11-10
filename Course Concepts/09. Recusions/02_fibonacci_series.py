def fibonacci(pos):
    assert (
        type(pos) == int and pos >= 0
    ), "The position should be a positive integral value"
    if pos in [0, 1]:
        return pos
    return fibonacci(pos - 1) + fibonacci(pos - 2)


val = int(input("Enter the position in the element in FS: "))
print(fibonacci(val - 1))
