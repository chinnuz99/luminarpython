#lim (min,max)read ,then  find sum of prime number
min=int(input("enter the initial lim"))
max=int(input("enter the final lim"))
sum=0
for a in range(max,min):
    if a>1:
        for i in range(2, a):
            if(a % i) ==0:
                break
        else:
            print(a)
            sum += a
print("sum of prime number in",min ,"to", max,"is",sum)







