list=[2,3,5,7,4,6,1]
print(list)
prime=[]
nonprime=[]
for i in list:
    if(i>1):
        for j in range(2,i):
            if(i%j==0):
                nonprime.append(i)
                break
        else:
            prime.append(i)
print("prime",prime)
print("nonprime",nonprime)
