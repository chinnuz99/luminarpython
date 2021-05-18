arr=[2,3,4,5,5,6]
squares=[num**2 for num in arr]
print(squares)

#[('mango','mango'),("
fruits=["mango","apple","orange"]
pairs=[(fruit,fruit) for fruit in fruits]
print(pairs)

lst1=[1,2]
lst2=[10,20]
pairs=[(num1,num2)for num1 in lst1 for num2 in lst2]
print(pairs)

lst2=[10,11,12,13,14]
evens=[num for num in lst2 if num%2==0]
print(evens)

lst2=[7,8,9,4,2]
patterns=[num+1 if num>5 else num-1 for num in lst2]
print(patterns)
