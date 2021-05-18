#given a list of integers,,write a program to calculate and display the
#sum of all the odd numbers in the list.
a=[2,8,3,6,4,1,7,9,5]
sum=0
for i in a:
    if(i%2==1):
        sum=sum+i
print(sum)

