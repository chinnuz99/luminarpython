import re
x='[0-9]'                # check digits
matcher= re.finditer(x,"ab11Zt ch4zAbn")
for match in matcher:
    print(match.start())
    print(match.group())