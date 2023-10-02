# The use of all() function

# the function returns boolean value depending upon the keys present in the dictionary
# the function follows AND truth table

# case 1: For all keys to be non-zero
case1 = {
    1:'one',
    2:'two',
    3:'three',
    4 :'four',
    5 :'five',
    6 :'six',
    7 :'seven',
    8 :'eight'
}
print(all(case1))



# case 2: When one of the keys is zero
case2 = {
    1:'one',
    0:'zero',
    3:'three',
    4 :'four',
    5 :'five',
    6 :'six',
    7 :'seven',
    8 :'eight'
}
print(all(case2))


# case 3: When all the keys are Zero
case3 = {
    False:'error',
    0:'zero',
    
}
print(all(case3))
