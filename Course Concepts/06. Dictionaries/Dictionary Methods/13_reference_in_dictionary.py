''' 
If theres a dictionary which which we want to be get referenced and is assigned to a new variable
This results referencing of the original dictionary with the new varible name

Now, if we perform change in the new dictionary, the same will be reflected into the original dictionary
Since, both are pointing to the same dictionary and vice-versa
'''

original = {
    1:'one',
    2:'two',
    3:'three',
}

#referenced the original dictionary to a new variable 
nakli = original 

# made change in the value assumed to be copied new dictionary 
nakli[1]='five'  
original[2]='tejas'

#changes are seen into the orginal dictionary too
print(original[1])
print(nakli[2])