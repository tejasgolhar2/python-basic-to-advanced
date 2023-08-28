import random
import emoji

def print_map(p_map):
    print('\n'.join([' '.join(['{:3}'.format(item) for item in row]) for row in p_map]))


# The :2 specifies that the item should be formatted to take up at least 
# 2 characters of width. If the item's length is less than 2 characters, 
# it will be padded with spaces on the left to meet that width.

map1 = [["⬜️","️⬜️","️⬜️"],["⬜️","️⬜️","️⬜️"],["⬜️","️⬜️","️⬜️"]]
print("This is our initial map...")
print_map(map1)

# random position of golden star
val1 = random.randint(1,3)
val2 = random.randint(1,3)
map1[val2-1][val1-1] = "⭐️"

# ask user to predict star
number = input("What do you think: where is the Golden Star in the map? ")
col = int(number[1])
row = int(number[0])
if (val1==col and val2==row)or(val1==row and val2==col):
    print("Congratulations!!! You have found the Golden STAR!")
    print_map(map1)
else:
    print("Unfortunatly you could find it 🙁")
    map1[col-1][row-1]="🆇"
    print_map(map1)

