#using forloop odd to even number  and check sum
low=int(input("enter the low limit"))
upp=int(input("enter the upp limit"))
evensum=0
oddsum=0
for i in range(low,upp+1):
    if(i%2==0): #1%2==0
        evensum+i
    else:
        oddsum+i
print(evensum)
print(oddsum)