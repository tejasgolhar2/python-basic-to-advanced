
# we aim to convert the received name into "TITLECASE"

def print_formatted_name(a,b):
    formatted_name = a.title()
    formatted_surname = b.title()

    result = (f"{formatted_name} {formatted_surname}")
    return result

    print("This won't be printed")

# Whatever content is written after the return statement of the function, that part of the code wont be executed

name = input("Enter name: ")
surname = input("Enter surname: ")

output = print_formatted_name(a=name,b=surname)
print(output)

