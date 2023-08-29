# USE OF SPLIT FUNCTION IN PYTHON
# the split function in Python is used to split a given list with elements separted with separator

str1 = "Tejas is doing his best"

# list with elements as individual string characters
list1 = list(str1)
print(list1)

# list with elements as set of characters separated by separator
list2 = str1.split(" ")
print(list2)


# USE OF JOIN FUNCTION IN PYTHON (  LIST TO STRING CONVERSION )
#    the join function is lists is used to join the elements of the list with a separator in between the elements
#    the join function only works with the string values

list3 = ['Ram','and','Shyam','are','best','friends']

#join1
new_list1 = " ".join(list3)
print(new_list1)

#join2
new_list2 = "_".join(list3)
print(new_list2)