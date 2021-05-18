list=[1,53,4,96,46]
print(list)
oddset=set()
evenset=set()
for i in list:
    if(i%2==0):
        evenset.add(i)
    else:
        oddset.add(i)
print("even set",evenset)
print("odd set",oddset)