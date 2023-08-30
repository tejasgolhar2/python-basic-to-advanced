# Multiply Dictionary Items
# Implement a function which takes dictionary as a parameter and returns multiplication of values of this dictionary.

# Example

# my_dict = {"One" : 1, "Two" : 2, "Three" : 3, "Four" : 4}
# multiply_values(my_dict)
# Output

# 24

def multiply_values(p_dict):
    ans = 1
    for item in p_dict:
        ans *= p_dict[item]
    return ans
    
    
my_dict = {"One" : 1, "Two" : 2, "Three" : 3, "Four" : 4}
print(multiply_values(my_dict))