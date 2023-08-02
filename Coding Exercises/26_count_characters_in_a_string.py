#       Implement a function count_letter that takes 
# two parameters : a string and a letter, 
# then returns the  number of times the letter  appears in a string

def count_letter(word, letter):
    count = 0
    for char in word:
        if letter==char:
            count+=1
    return count

ans = count_letter("Learning Python", "n")
print(ans)