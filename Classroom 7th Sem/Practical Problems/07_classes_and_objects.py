# 7. Write a program to demonstrate the implementation of classes and objects.


# Define a simple class called 'Person'
class Person:
    # Constructor method to initialize the object's attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method to display information about the person
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Create an instance (object) of the Person class
person1 = Person("John", 25)

# Access and modify object attributes
print(f"Before modification - Name: {person1.name}, Age: {person1.age}")
person1.age = 26  # Modify the 'age' attribute
print(f"After modification - Name: {person1.name}, Age: {person1.age}")

# Call a method of the object
person1.display_info()
