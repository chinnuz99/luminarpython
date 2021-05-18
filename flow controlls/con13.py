#three number read,
#second largest element#100,80,50 ans 80
num1=int(input("enter the num1"))
num2=int(input("enter the num2"))
num3=int(input("enter the num3"))
if(num1>num2)&(num1>num3):
    if(num2>num3):
         print(num2,"second largest number")
    else:
         print(num3,"second largest")
elif(num2>num3)&(num2>num1):
     if(num1>num3):
         print(num1)
     else:
         print(num3)
elif(num3>num1)&(num3>num2):
    if(num1>num2):
         print(num1)
    else:
         print(num2)

