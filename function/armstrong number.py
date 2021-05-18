num=int(input("enter number"))#153=1*1*1 + 5*5*5 + 3*3*3 //153
sum=0
temp=num
while(temp>0): #153>0
    digit=temp%10 #153%10=15
    sum+=digit**3 #0+=15**3
    temp//=10 #153//10=3
if(sum==num):
    print(num,"is armstrong number")
else:
    print(num,"is not armstrong number")

