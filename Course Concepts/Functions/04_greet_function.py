#function without name passing
'''def greet():
    print("Hello !")
    print("How are you ?")

greet()'''

#function with passing of name
def greet_with_name(name):
    print(f"Hello {name}!") 
    print(f"How are you {name}?")

naam = input("Enter your name please: ")
greet_with_name(naam)
