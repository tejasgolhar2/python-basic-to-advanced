# Base class (parent class)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

# Derived class (child class)
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Derived class (child class)
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Create instances of the derived classes
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Demonstrate inheritance
print(dog.speak())  # Output: Buddy says Woof!
print(cat.speak())  # Output: Whiskers says Meow!
