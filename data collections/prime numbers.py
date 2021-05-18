#create prime numbers set
s={2,1,8,7,9,5,6}
print(s)
prime=set()
nonprime=set()
for i in s:
    if(i>1):
        for j in range(2,i):
            if(i%j==0):
                nonprime.add(i)
                break
        else:
            prime.add(i)
print("prime",prime)
print("nonprime",nonprime)


