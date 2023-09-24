# Concept of Shallow Copy

# The need arises when the items in the dictionary are mutable 
#       Considering the mutable item to be a 'list',
#        If there are multiple lists in the dictionary and we made a copy of
# the dictionary, copy is made for dictionary and not the lists. When we try changing one of the list in 
# the original dictionary, the same changes are reflected as the change in all the dictionaries

# This means that, both copies of dictionaries are referencing to the same lists

name_list = ["Edy", "John", "Ewan"]
city_list = ["London", "Berlin", "Paris"]
language_list = ["Enlish", "German", "French"]

person = {
    "name" : name_list,
    "city" : city_list,
    "language" : language_list,
}

new_person = person.copy()

person["city"].append("Appended using person dict")

new_person["city"].append("Appended using new person dict")

city_list.append("Append by itself") 

# All the following will have the same output since all are referencing to the same lists
print(person["city"])
print(new_person["city"])
print(city_list)
