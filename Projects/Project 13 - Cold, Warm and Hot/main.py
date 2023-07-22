def temperature(val):
    if (val>28):
        return "Hot"
    if ((val>=18)and(val<=28)):
        return "Warm"
    if val<18:
        return "Cold"

value = float(input("Enter temperature: "))
print(temperature(value))