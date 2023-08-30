
# Generate Dictionary
# Implement a function which takes integer number (n) as a parameter and returns dictionary with keys from 1 to n and values are square of the numbers from 1 to n.

# Example

# generate_dictionary(5)

# Output

# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

def generate_dictionary(val):
    dict1 = dict()
    for item in range(1,val+1):
        dict1[item] = item ** 2
    print(dict1)
    
    
generate_dictionary(5)