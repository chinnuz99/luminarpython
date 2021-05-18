import re
x='\D'                   #except digits
matcher= re.finditer(x,"ab11Zt ch49zAbn")
for match in matcher:
    print(match.start())
    print(match.group())