# 8. Write a program to demonstrate the concept of inheritance


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass  # Abstract method, to be overridden by subclasses


class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"


class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"


# Creating instances of the derived classes
dog_instance = Dog("Buddy")
cat_instance = Cat("Whiskers")

# Calling the speak method on the instances
print(dog_instance.speak())  # Output: Buddy says Woof!
print(cat_instance.speak())  # Output: Whiskers says Meow!
