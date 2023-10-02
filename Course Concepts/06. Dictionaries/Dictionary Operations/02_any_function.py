# Use of any() function in Python

# This function works similar to that of the all()
# This funtion returns boolean value depending upon the keys present in the dictionary
# It follows OR truth table

# Case 1: When all keys are true
case1 = {
    1 :'one',
    2 :'two',
    3 :'three',
    4 :'four',
    5 :'five',
    6 :'six',
    7 :'seven',
    8 :'eight'
}
print(any(case1))


# Case 2: When oen among the keys is false
case2 = {
    1 :'one',
    0 :'zero',
    3 :'three',
    4 :'four',
    5 :'five',
    6 :'six',
    7 :'seven',
    8 :'eight'
}
print(any(case2))


# case 3: When all the keys are Zero
case3 = {
    False:'error',
    0:'zero',
    
}
print(any(case3))
