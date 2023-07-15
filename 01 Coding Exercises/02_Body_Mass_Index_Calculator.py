"""Write a program that calculates the Body Mass Index (BMI) 
based on a user's weight and height and interprets it.

It should tell them the interpretation of their BMI based on the BMI value.

Under 18.5 they are underweight
Over 18.5 but below 25 their weight is normal
Over 25 but below 30 they are overweight
Over 30 but below 35 they are obese

"""

height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
# TODO

bmi = weight / pow(height, 2)
# bmi = range(int(bmi),2)
# print(f"Your bmi is {round(bmi,2)}")

if bmi < 18.5:
    print(f"Your bmi is {round(bmi,2)}, your weight is underweight.")

elif (bmi > 18.5) and (bmi < 25):
    print(f"Your bmi is {round(bmi,2)}, your weight is normal.")

elif (bmi > 25) and (bmi < 30):
    print(f"Your bmi is {round(bmi,2)}, your weight is overweight.")

else:
    print(f"Your bmi is {round(bmi,2)}, your weight is obese.")
