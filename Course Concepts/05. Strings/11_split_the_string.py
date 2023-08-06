# To split the object into corresponding substrings separated by spaces  >> BY DEFAULT
# The splitted substrings are obtained as a comma separated list 


# DEFAULT STRING SPLIT

des = "Tejas is a boy"
print(des.split())

des1 = "Tejas is a good boy"
value1 = des1.split(" ")
print(value1) 

#  means split the substrings from the variable where spaces are found
# both above are the same


# STRING SPLIT AS PER THE SEPARATION CHARACTER

des2 = "Tejas_is_a_very_good_boy"
value2 = des2.split("_")
print(value2)

# split the variable from the places in the variable where '_' is present


# STRING SPLIT WITH LIMITATIONS ON SPLITS

des2 = "Tejas_is_a_very_very_good_boy"
print(des2.split("_", maxsplit = 2))  


# TO JOIN THE ELEMENTS OF THE LIST

result1 = " ".join(value1)
result2 = "_".join(value1)
result3 = " ".join(value2)
result4 = "_".join(value2)

print(result1)
print(result2)
print(result3)
print(result4)
