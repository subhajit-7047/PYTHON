weight=float(input("Enetr weight:"))
height=float(input("Enetr height:"))

bmi=round(weight/height**2)

if bmi<18.5:
    print(f"Your bmi is {bmi} and you are underweight.")
elif bmi<25:
    print(f"your bmi is {bmi} and you have a normal weight.")
elif bmi<30:
    print(f"your bmi is {bmi} and you are overweight.")
elif bmi< 35:
    print(f"your bmi is {bmi} and you are Obese.")
else:
    print(f"your bmi is {bmi} and you are clinically obese.")