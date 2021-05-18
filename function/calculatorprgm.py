#calculator
def add(x,y):
    return(x+y)
def sub(x,y):
    return(x-y)
def mul(x,y):
    return(x*y)
def div(x,y):
    return(x/y)
print("select operation")
print("1.addition")
print("2.substraction")
print("3.multiplication")
print("4.division")
while True:
    choice=input("enter the choice")
    if choice in('1','2','3','4'):
        num1=float(input("enter a number"))
        num2=float(input("enter a number"))
        if choice=='1':
            print(add(num1,num2))
        elif choice=='2':
            print(sub(num1,num2))
        elif choice=='3':
            print(mul(num1,num2))
        elif choice=='4':
            print(div(num1,num2))
        break
    else:
     print("invalid")







