import re
x='^a'                     #check starting with a
r="aaa abc aaaa cga"
matcher= re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())