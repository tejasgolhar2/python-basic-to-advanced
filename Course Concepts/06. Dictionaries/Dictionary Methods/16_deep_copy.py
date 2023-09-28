# CONCEPT OF DEEP COPY

#       This results in changes in the copied dictionary only and doesn't affect the original one
#    It uses the inclusion of the "copy" library

import copy


name_list = ["Edy", "John", "Ewan"]
city_list = ["London", "Berlin", "Paris"]
language_list = ["Enlish", "German", "French"]

#original dictionary
person = {
    "name" : name_list,
    "city" : city_list,
    "language" : language_list,
}

#deep-copying the original one
new_person = copy.deepcopy(person)

#changes done in iterable of the original object
person["city"].append("Appended using person dict")

#changes done in the iterable of the deep-copied object
new_person["city"].append("Appended using new person dict")

#changes done in iterable as the object itself
city_list.append("Append by itself") 


# Only the changes as per the calling of dictionary is done 
print(person["city"])
print(new_person["city"])
print(city_list)
