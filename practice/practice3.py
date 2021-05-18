#program to accept three integers and print the largest of the three. make use of
#only if statement.
x=float(input("enter the first number:"))
y=float(input("enter the second number:"))
z=float(input("enter the third number:"))
max=x
if(y>max):
    max=y
if(z>max):
    max=z
print("largest number is", max)