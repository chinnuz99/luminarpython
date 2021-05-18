#content in a to b
#a="abc"
#b=" "
a="abc"
b=" "
for i in a:
    if i not in b:
        b+=i
print(b)

