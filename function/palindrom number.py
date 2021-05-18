num=int(input("enter the number"))
sum=0
rev=0
temp=num
while(temp>0):
    digit=temp%10
    rev=(rev*10)+digit
    temp//=10
if(num==rev):
    print(num,"is palindrome")
else:
    print(num,"is not palindrome")


