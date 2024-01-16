# Exercise 9 - BMI 2.0

height = float(input())
weight = int(input())

weight_as_int = int(weight)
height_as_float = float(height)

bmi = weight_as_int / height_as_float ** 2

if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif 25 > bmi >= 18.5:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif 30 > bmi >= 25:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif 35 > bmi >= 30:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")