height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

float_height = float(height)
int_weight = int(weight)

#BMI
bmi = int(int_weight / float_height**2 )

print(bmi)