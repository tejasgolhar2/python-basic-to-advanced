# Find Numbers Divisible by 3 and 4
#       Implement a function which takes a parameter N and returns 
#   Set of numbers which are divisible by 3 and 4 between 0 and N.

# Example Input

# divisible_by_3and4(100)

# Output

# {0, 96, 36, 72, 12, 48, 84, 24, 60}


def divisible_by_3and4(v_num):
    set1 = set()

# Logic 1 : Using the divisibility test
    # for i in range(v_num+1):
    #     if ((i%3==0) and (i%4==0)) == True:
    #         set1.add(i)
    # return set1

# Logic 2: Using the set intersection property
    set_3 = set(range(0,v_num+1,3))
    set_4 = set(range(0,v_num+1,4))
    set1 = set.intersection(set_3,set_4)
    return set1
    
print(divisible_by_3and4(100))