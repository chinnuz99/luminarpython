#programe for calculator
print("1.ADDITION")
print("2.SUBSTRACTION")
print("3.MULTIPLICATION")
print("4.DIVISION")
print("5.EXPONEnt")
opt=int(input("enter ur option"))
num1=int(input("enter num"))
num2=int(input("enter num"))
if(opt==1):
    print(num1+num2)
elif(opt==2):
    print(num1-num2)
elif(opt==3):
    print(num1*num2)
elif(opt==4):
    print(num1/num2)
elif(opt==5):
    print(num1^num2)
else:
    print("error")


