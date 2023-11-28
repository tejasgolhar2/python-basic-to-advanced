# Sum of Positive Integers
#           Implement a function to calculate the sum of the positive integers 
#       of n+(n-2)+(n-4)... (until n-x =< 0).

# Example

# sum_positive(10)

# Output

# 30

def sum_positive(v_num):
    if v_num<0:
        return 0
    else:
        return v_num + sum_positive(v_num-2)

print(sum_positive(10))