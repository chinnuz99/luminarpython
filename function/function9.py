#a="luminar" ,one letter read
a="luminar"
b=input("enter the letter")
flag=0
for i in a:
    if i in b:
        flag=1
if flag==1:
    print("present")
else:
    print("not preesent")