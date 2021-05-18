#enter the string heello
#the count of vowels in heello is=3
a=input("enter string")
count=0
for i in a:
    if i in ('a','e','i','o','u'):
        count+=1
print(count)


# a=input("enter the string")
# count=0
# for i in a:
#     if i in('aeiou'):
#         count+=1
#     else:
#         pass
#print(count)