#number read
#153
#351
#153%10=3,153//10=15,15%10=5,15//10=1,1%10=1
num=int(input("enter the num")) #153
res=0
while(num!=0): #153!=0 15!=0
    digit=num%10 #153%10=3 ,15%10=5
    res=(res*10)+digit #(0*10)+3=3,
    num=num//10 #153//10=15
print(res)
