import re
n="56kg"
x='\d{2}[a-z]{2}'       #x='\d' check the digits,x='[a-z]' a to z,a{2}' 2 no of a position
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")
#x='[^a-zA-ZO-9]'special symbols