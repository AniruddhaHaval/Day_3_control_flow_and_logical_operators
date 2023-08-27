height = float(input("Enter your height in meter: "))

weight = int(input("Enter weight in kg: "))

bmi = float("{:.2f}".format(weight / (height**2)))

if bmi < 18.5:
    print(f"Your  bmi is {bmi}. You are underweight.")
elif bmi < 25:
    print(f"Your  bmi is {bmi}. You have a normal weight.")
elif bmi < 30:
    print(f"Your  bmi is {bmi}. You are slightly overweight.")
elif bmi < 35:
    print(f"Your  bmi is {bmi}. You are obese.")
else:
    print(f"Your  bmi is {bmi}. You are clinically obese.")
