'''
    Define a function that converts fluid ounces 
to milliliters and prints the result to the console. 
    Take into account that 1 fluid ounce is equal 
to 29.57353 milliliters.

'''

def volume_converter(ounce):
    mlltr = 29.57353 * ounce
    print(mlltr)

volume_converter(5)