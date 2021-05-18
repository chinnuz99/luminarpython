#filter python student id from text file and
import re
lst=[]
f=open("rulevalidation","r")
x='^[L][U][M]\d{2}[P][Y]\d{3}'
for i in f:
    m=re.findall(x,i)
    if m!=[]:
        lst.append(m)
        w=open("rulevalidation.txt","w")
        w.write(str(lst))
