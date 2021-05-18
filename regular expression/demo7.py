import re
x='[^a-zA-ZO-9]'         #special symbols
matcher= re.finditer(x,"ab11Zt ch49zAbn")
for match in matcher:
    print(match.start())
    print(match.group())