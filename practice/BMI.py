#program to calculate bmi(body mass index) of a person. body mass index is a simple
#calculation using a person's height and weight.the formula is BMI=kg/m2 where kg is a
#person's weight in kilograms and m2 is their height in meters squared.
weight_in_kg=float(input("enter the weight in kg:"))
height_in_meter=float(input("enter the height in meters:"))
bmi=weight_in_kg/(height_in_meter*height_in_meter)
print("BMI is :",bmi)
