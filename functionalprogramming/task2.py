#lst1=[10,20,21,22,23]
# lst2=[20,21,10,22,23]
# check for given list are same or not
lst1=[10,20,21,22,23]
lst2=[20,21,10,22,23]
flag=0
for i in lst1:
    for j in lst2:
        if i==j:
            flag=1
if flag==1:
    print("same")




