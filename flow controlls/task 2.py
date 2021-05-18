y1=int(input("enter the current year"))
m1=int(input("enter the current month"))
d1=int(input("enter the current date"))
y2=int(input("enter the birth year"))
m2=int(input("enter the birth month"))
d2=int(input("enter the birth date"))
if(m2!=m1)&(m2>m1):
    m=m1+(12-m2)
else:
    m=m2-m1
if(y1!=y2)&(y1<y2):
    y=(y1-y2-1)
else:
    y=y1-y2
if(d1!=d2)&(d1<d2):
    d=d2-d1
else:
    d=d1-d2
    print("you",y,"years",m,"months",d,"days old")



