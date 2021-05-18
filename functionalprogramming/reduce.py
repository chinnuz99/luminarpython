 #reduce
 # import functools
from functools import *
arr=[1,2,3,4,5,6]
total=reduce(lambda num1,num2:num1+num2,arr)
print(total)
#print highest number
highest=reduce(lambda num1,num2:num1 if num1>num2 else num2,arr)
print(highest)
