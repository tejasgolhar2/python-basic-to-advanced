# Delete Restricted Items
#   Set of items and set of restricted items are given, based on the beach type 
# (family or normal) the list of items should be printed to the console. 
#       Restricted items are not allowed to family beach and everything else 
# can be taken to normal beach except drugs.

general_items = {
    "Sand toys",
    "Beach towels",
    "Beach umbrella",
    "Camp chair",
    "Snacks",
    "Hats",
    "Camera",
    "Sunglasses",
    "Alcholic Drinks",
    "Non Alcholic Drinks",
    "Sigarettes",
    "Sharp Objects"
}
 
restricted_items = {
    "Non Alcholic Drinks",
    "Sigarettes",
    "Sharp Objects",
    "Amplified Audio",
    "Drugs"
    }
choice = int(input("Select Beach Type (1 - Family beach, 2 - Normal Beach):"))

print("See below the list of items that you can take.")

if choice==1:
    for element in restricted_items:
        general_items.discard(element)
elif choice==2:
    general_items.discard("Drugs")
    
for item in general_items:
    print(f"\t{item}")


# Example Input

# Select Beach Type (1 - Family beach, 2 - Normal Beach): 1

# Example Output

# See below the list of items that you can take.
#     Alcholic Drinks
#     Sand toys
#     Snacks
#     Sunglasses
#     Hats
#     Beach umbrella
#     Beach towels
#     Camp chair
#     Camera