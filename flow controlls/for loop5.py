#using for loop low to upper even numbers
low=int(input("enter the low lim"))
upp=int(input("enter the upp lim"))
for i in range(low,upp+1):
    if(i%2==0):
        print(i)
