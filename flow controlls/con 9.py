num1=int(input("enter the classes held"))
num2=int(input("enter the classes attended"))
avg=(num2/num1)*100
print(avg)
if(avg>=75):
    print("allowed")
else:
    print("not allowed")