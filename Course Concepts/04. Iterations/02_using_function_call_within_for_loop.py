def checkValidity(state):
    if len(state)>=6:
        print(f"{state} represents valid set of characters")
    else:
        print(f"{state} represents invalid set of characters")


states_in_India = ["Mizoram","Assam","Andra Pradesh","Arunachal Pradesh","Chhatisgarh"]
for state in states_in_India:
    ref = state.title() #function call within for loop
    checkValidity(ref)