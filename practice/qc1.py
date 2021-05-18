a=int(input("enter the number"))
def num(a):
    if(a>10):
        print("the",a,"is greater than 10")
    elif(a==10):
        print("the",a,"is equal to 10")
    elif(a<10):
        print("the",a,"is less than 10")
while True:
    num(a)
    break

