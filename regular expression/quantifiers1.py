import re
x='a+'                     #a including group
r="aaa abc aaaa cga"
matcher= re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())