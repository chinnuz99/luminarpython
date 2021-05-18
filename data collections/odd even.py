# to add odd and even elemnts to different set
s={1,8,5,9,4,7,11,100,5,}
print(s)
odd=set()
even=set()
for i in s:
    if(i%2==0):
        even.add(i)
    else:
        odd.add(i)
print("even set",even)
print("odd set",odd)

