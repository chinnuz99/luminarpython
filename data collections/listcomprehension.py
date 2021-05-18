## list comprehensions are used for creating new lists from other iterables.
## as list comprehensions return list,they consist of brackets containing the expressions.
## which is executed for each element along with the for loop to iterate over each element.
a=[2,5,8,4,4,6,8]
print(a)
s=1
b=[]
for i in a:
    s=i*i
    b.append(s)
print(b)
 # list comprehension method
a=[1,2,3,4,5,6]
squares=[n**2 for n in a]
print(squares)