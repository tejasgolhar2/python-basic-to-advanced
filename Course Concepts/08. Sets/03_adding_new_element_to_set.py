# Adding new element to set

my_set = set()

# Lets add element one-by-one

# New element is added
my_set.add(1)
my_set.add(2)
my_set.add(3)
print(my_set)


# Repeated/Duplicate Element is tried to be added
# It doesn't result any error.
my_set.add(1)
print(my_set)

# Demonstrate : No duplicates are stored
# A loop that take 5 different values from user
new_set = set()

while len(new_set)<4:
    new_set.add(input("Enter a unique set element: "))

print(new_set)