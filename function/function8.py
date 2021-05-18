#pyramid pattern
def pattern(n):
    for i in range(0,n):
        for j in range(i+1,n):
            print("*",end=" ")
        print("\r")
pattern(6)