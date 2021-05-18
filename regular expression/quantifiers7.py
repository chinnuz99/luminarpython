import re
x='a$'                     #doller symbol($)#check ending with a
r="aaa abc aaaa cgba"
matcher= re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())