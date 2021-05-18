#write a program to input a list of numbers and swap elements at the even
#location with the elements at the odd location.
a=[2,8,9,3,6,7,64,56,4,23]
print(a)
s=len(a)
if(s%2!=0):
    s=s-1
for i in range(0,s,2):
        print(i,i+1)
        a[i],a[i+1]=a[i+1],a[i]
print("list after swapping:",a)

