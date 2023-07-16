name_1 = input("Enter first name: ")
name_2 = input("Enter second name: ")

name1 = name_1.lower()
name2 = name_2.lower()

# len1 = len(name1)
# len2 = len(name2)

# for the word love
t = name1.count("t") + name2.count("t")
r = name1.count("r") + name2.count("r")
u = name1.count("u") + name2.count("u")
e1 = name1.count("e") + name2.count("e")

l = name1.count("l") + name2.count("l")
o = name1.count("o") + name2.count("o")
v = name1.count("v") + name2.count("v")
e2 = name1.count("e") + name2.count("e")

count = int(str(t + r + u + e1) + str(l + o + v + e2))

if (count < 10) or (count > 85):
    print(f"Your score is {count}, you go together like coke and mentos.")
elif (count >= 40) and (count <= 70):
    print(f"Your score is {count}, you are alright together.")
else:
    print(f"Your score is {count}.")
