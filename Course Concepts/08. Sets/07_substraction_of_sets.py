
fruits = {"apple", "pear", "limon", "grape", "cucumber", "orange"}
vegetables = {"cucumber", "garlic", "onion", "broccoli", "pepper"}

# Subtracting - The result is the elements of the first set which are not present in the second set
# The order of syntax specification of subtraction changes the answer 


# Method 1

sub1 = fruits.difference(vegetables)  # Subtract 2nd Set from 1st
print(sub1)

sub2 = vegetables.difference(fruits)  # Subtract 1st Set from 2nd
print(sub2)


# Method 2

sub3 = fruits - vegetables
print(sub3)

sub4 = vegetables - fruits
print(sub4)

# NOTE : The Set subtraction can be implemented in 'Coding Exercises\60_delete_restricted_items.py' 