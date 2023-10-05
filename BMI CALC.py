#BODY MASS INDEX CALCULATOR


#PARAMETERS
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))


#FORMULA
BMI = (weight / (height ** 2))
BMI = round(BMI, 2)


print(f"Your BMI is {BMI}")








