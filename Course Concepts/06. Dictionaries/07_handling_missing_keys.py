#   HANDLING MISSING KEYS INSIDE DICTIONARY
#       The user not always is known with the key value whether present in the dictionary or not
#   If tried accessing the key not present in the dictionary, it results KeyError
#   How to handle these missing keys in the dictionary ?


# Method 1: Use of .get() method
#    --->>  It returns the value of the searched key in the dictionary
#    --->>  The key searched doesn't modify the original dictionary
#    --->>  Results None, if the value not present and donesn't produce any error
#    --->>  We can put a default value for keys not present in the dictionary

equipments = {
    'computer':10,
    'laptops': 5,
    'mouse':20,
    'speakers':40,
    'keyboards':21,
}
value = equipments.get("extensions",0)
print(f"The number of extensions in the equipments : {value}")
print(equipments)


# Method 2: Use of .setdefault() method
#    --->>  It returns the value of the searched key in the dictionary
#    --->>  Results None, if the value not present and donesn't produce any error
#    --->>  We can put a default value for keys not present in the dictionary
#    --->>  The key searched is added at the dictionary

equipments1 = {
    'computer':1,
    'laptops': 15,
    'mouse':25,
    'speakers':41,
    'keyboards':15,
}
quantity = equipments1.setdefault("microphone",0)
print(f"The number of microphone in the second equipments list : {quantity}")
print(equipments1)