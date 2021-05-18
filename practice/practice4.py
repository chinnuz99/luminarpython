#program to find the divisibility of a numbernwith another number(i.e a
# number is divisible by another.)
num1=int(input("enter first number"))
num2=int(input("enter the second number"))
r=num1%num2
if(r==0):
    print(num1,"is divisible by",num2)
else:
    print(num1,"is not divisible by",num2)