# the copy method is used to copy a list 
# the method returns a new list which is the copy of the given list

names = ["Neha","Ravi","Shashikant","Rubina","Ahemad","Jatin","John"]
print("Original List\n",names)
new_list = names.copy()
print("Copied List\n",new_list)

names.append("Karishma")
print("Modification in base list")
print(new_list)

# modification done in original list is not reflected into the copied list



# ALTERNATE APPROACH
# instead of using copy method, we can use assignment operator to copy a given list

# NOTE: modifications done in the original list are reflected in the modified list

names2 = ["Rubina","Ahemad","Jatin","John"]
print("Original List\n",names2)

modified_list = names2
print("Assigned List\n",modified_list)

names2.append("Karishma")
print("Modification in base list")
print(modified_list)

