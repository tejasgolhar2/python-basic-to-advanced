##  Moving forward from the concept of referencing in dictionaries,
# In order to prevent the changes in the dictionary, the copy method is implied

original = {
    1:'one',
    2:'two',
    3:'three'
}
nakli = original.copy()

#changes in duplicate are not seen in original
nakli[3]='kunal'
print(original[3])

#changes in original are not seen in duplicate
original[2]='shambhu'
print(nakli[2]) 