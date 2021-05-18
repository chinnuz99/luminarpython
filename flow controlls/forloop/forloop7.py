#check the given number is prime
#9 2to 8
num=int(input("enter the num")) #9
flag=0
for i in range(2,num): #2,9-1=8 ,3
    if(num%i==0):#9%2==0 false, 9%3==0 true
        flag=1 #1
if(flag>0):
    print("not a prime")
else:
    print("prime")