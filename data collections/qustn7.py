#given the nested if-else below,what will be the value x when the code executed
#successfully.
x=0
a=5
b=5
if a>0: #5>0
    if b<0: #5<0
        x=x+5 #x=0+5=5
    elif a>5: #5>5
        x=x+4 #0=0+4=4
    else:
        x=x+3 #0=0+3=3
else:
    x=x+2 #0=0+2=2
print(x)
