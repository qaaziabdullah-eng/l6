print("BMI calculator \n")
w=int(input("enter your weight in kg: "))
h=float(input("enter your height in meter: "))
bmi=w/(h*h)
print("your bmi is: ",bmi)
if bmi<18.5:
    print("you are underweight")

elif bmi>=18.5 and bmi<25:
    print("you have normal weight")

elif bmi>=25 and bmi<30:
    print("you are overweight")
else:
    print("you are obese")

