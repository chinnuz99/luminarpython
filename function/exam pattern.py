# 1
# 1 1
# 1 1 1 1
# 1 1 1 1 1
# 1 1 1 1 1 1
# 2 2 2 2 2 2
# 2 2 2 2 2
# 2 2 2 2
# 2 2 2
# 2 2
# 2
# 3
# 3 3
# 3 3 3
a=int(input("enter the initial range")) #4
b=int(input("enter the final range")) #6
for i in range(a,b):
    if(i%2==0):
        r=6
        for k in range(r,0,-1):
            for j in range(0,k):
                print(i,end=" ")
            print("\r")
    else:
        r2=6
        for l in range(r2): #(6)
            for m in range(0,l+1):
                print(i,end=" ")
            print("\r")

