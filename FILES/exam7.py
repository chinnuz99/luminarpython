import re
lst=[]
f=open("exam7","r")
x='[+][9][1]\d{10}'
for i in f:
    m=re.findall(x,i)
    if m!=[]:
     lst.append(m)
     w=open("exam7.txt","w")
     w.write(str(lst))

