#lower limit upper limit read
#lower to upper even numbers read
low=int(input("enter the lower limit")) #2
upp=int(input('enter the upper limit')) #8
while(low<=upp): #2<=8 ,3<=8
    if(low%2==0):#2%2==0,ans=8, 3%2==1.5,ans=1.5(false)
        print(low) #2
    low+=1