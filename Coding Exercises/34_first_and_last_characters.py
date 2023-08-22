# First and Last Characters
# Implement a function which takes the string type list as a parameter and returns the count of the number of strings where the string length is 2 or more and the first and the last characters are same.

# Example

# list1 = ['cbc', 'xyz', 'aba', '2332', 'abc']
# count_words(list1)
# Output

# 3

def count_words(p_list):
    # TODO
    count = 0
    for item in p_list:
        if (item[0]==item[-1])and(len(item) >=2):
            count+=1
    return count
            
list1 = ['cbc', 'xyz', 'aba', '2332', 'abc']
print(count_words(list1))