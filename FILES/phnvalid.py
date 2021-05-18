import re
r=open("phn","r")
f=open("num.txt","w")
rule="[+][9][1]\d{10}$"
for num in r:
  number=num.rstrip("\n")
  matcher=re.fullmatch(rule,number)
  if matcher!=None:
       f.write(number)
       f.write("\n")

