#a function its self is called  recursion
#fibnocci series using recursion
#call afunction inside the same function
#important
def recur_fibo(n):
    if n<=1:
        return n
    else:
        return recur_fibo(n-1)+recur_fibo(n-2)
nterms=10 #nterms=int(input("enter number))
if nterms<=0:
    print("please enter a positive integer")
else:
    print("fibonacci sequence:")
    for i in range(nterms):
        print(recur_fibo(i))

