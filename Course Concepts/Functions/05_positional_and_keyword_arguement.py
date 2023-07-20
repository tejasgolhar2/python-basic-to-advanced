# function with passing of name and city


# positional arguements

"""
        While passing the different arguements to a function during its call, 
    the positions of the passed values/arguements matters a lot.
        The first arguement will be passed to the first parameter in the function definition , 
    second to the second and so on..
    Such arguements are called Positional Arguements where the position of arguements to be passed matters.
       
        Disadvantages of Positional Arguements;
    The programmer may do mistake while calling the function and passing the arguements every time.
    To overcome the issue and confirm that the arguement should reach the intended parameter, keyword arguements are used.

"""


def greet_with_name(name, city):
    print(f"Hello {name}!")
    print(f"How is the weather like in {city}?")


naam = input("Enter your name please: ")
sheher = input("Enter your city: ")
greet_with_name(naam, sheher)


# keyword arguements
"""
The keyword arguements are the arguements with keywords assigned to them 
during the time of the function call itself so that theres no chance of mismatch 
even when the arguements are passed in mismatched positions.

"""


def greet_with_name(a, b):
    print(f"Hello {a}!")
    print(f"How is the weather like in {b}?")


naam = input("Enter your name please: ")
sheher = input("Enter your city: ")
greet_with_name(b=sheher, a=naam)
