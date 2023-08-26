# Extend Nested List
# Given a nested list and update the list with sub list ["h", "i", "j"] in such a way that it will look like the following list.

# list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']
# Output

# ist1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']

list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']
extra = ['h','i','j']

for item in extra:
    list1[2][1][2].append(item)

print(list1)

# Alternatively we can use Extend Method also