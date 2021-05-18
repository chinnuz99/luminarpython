a=int(input("enter first number"))
b=int(input("enter second number"))
oper=input("enter oper")

def cal(a,b,oper):
    if oper=="+":
        print (a+b)
    elif oper=="-":
        print (a-b)
    elif oper=="*":
        print (a*b)
    elif oper=="/":
        print (a/b)

while True:
    cal(a,b,oper)
    break













