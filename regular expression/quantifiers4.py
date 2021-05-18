import re
x='a{2}'                     # 2 no of a position   a{2}means 2a
r="aaa abc aaaa cga"
matcher= re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())