#lst1=[7,8,9,4,3,1]
# if num>5 num+1
# else num-1
#[8,9,10,3,2,0]

# lst=[7,8,9,4,3,1]
# op=[]
# for num in lst:
#     if num>5:
#         op.append((num+1))
#     else:
#        op.append((num-1))
# print(op)
# #
lst=[7,8,9,4,3,1]
op=[]
for num in lst:
     op.append((num+1)) if num>5 else op.append((num-1))    #terinary operator
print(op)
#lambda function have only single argument
op=list(map(lambda num:num+1 if num>5 else num-1,lst))
print(op)

#print even function
lst=[7,8,9,4,3,1]
evens=list(filter(lambda num:num%2==0,lst))
print(evens)
#lst comprehension
lst2=[7,8,9,4,2]
patterns=[num+1 if num>5 else num-1 for num in lst2]
print(patterns)

