# Comparing Tuples
# Implement a function which takes a string (sentence) as a parameter and returns a tuple in which the words from the given sentenced are ordered based on their length.

# Example

# order_words("Python is my favorite programming language")

# Output

# ('is', 'my', 'Python', 'favorite', 'language', 'programming')

def order_words(v_string):
    words = v_string.split()
    n_list = list()

    for item in words:
        n_list.append((len(item),item)) 

    n_list.sort()

    ans = list()
    for key,value in n_list:
        ans.append(value)
        
    return tuple(ans)

print(order_words("Python is my favorite programming language"))

