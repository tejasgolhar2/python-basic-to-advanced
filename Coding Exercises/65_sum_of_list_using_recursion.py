# Sum of List using Recursion
# Implement a function which takes a list as a parameter and calculates the sum of a list of numbers.

# sum_list([1, 2, 3, 4, 5])
# Output

# 15



def sum_list(v_list):
    if len(v_list)==0:
        return 0
    item = v_list[-1]
    v_list.pop(-1)
    return item + sum_list(v_list) 
    
print(sum_list([1, 2, 3, 4, 5]))