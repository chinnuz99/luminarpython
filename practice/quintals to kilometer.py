#write a program to input a value in tonnes and convert it into quintals and kilograms.
#*(1tonne-10quintals 1tonne=1000kgs,1 quintals=100kgs)
tonnes=float(input("enter the tonnes:"))
quintals=10*tonnes
kgs=quintals*100
print(tonnes)
print(quintals)
print(kgs)