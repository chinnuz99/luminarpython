#find common elements using for loop
s={1,3,5,7,89,2,3,4,56,6,7,1}
print(s)
s1={3,4,5,77,88,9,1}
print(s1)
for i in s:
    if i in s1:
        print(i)
